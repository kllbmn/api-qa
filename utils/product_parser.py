class ProductParserError(Exception):

    """상품 응답 파싱 과정에서 발생하는 예외"""

    pass


class ProductParser:

    # 현재 테스트에서 확인한 검색 결과 영역 코드

    SEARCH_RESULT_AREA_CODES = {

        "00001_000000010"

    }

    @staticmethod

    def extract_products(response_data):

        if not isinstance(response_data, dict):

            raise ProductParserError(

                "응답 데이터가 JSON 객체 형식이 아닙니다."

            )

        data = response_data.get("data")

        if not isinstance(data, dict):

            raise ProductParserError(

                "응답에 data 객체가 없습니다."

            )

        data_list = data.get("dataList")

        if not isinstance(data_list, list):

            raise ProductParserError(

                "dataList가 리스트 형식이 아닙니다."

            )

        products = []

        for unit in data_list:

            if not isinstance(unit, dict):

                continue

            if unit.get("unitType") != "ITEM_UNIT_LIST":

                continue

            # 검색 결과 영역만 추출

            if unit.get("tareaCd") not in (

                ProductParser.SEARCH_RESULT_AREA_CODES

            ):

                continue

            unit_products = unit.get("dataList", [])

            if not isinstance(unit_products, list):

                continue

            for product in unit_products:

                if isinstance(product, dict):

                    products.append(

                        ProductParser._normalize_product(product)

                    )

        return products

    @staticmethod

    def _normalize_product(product):

        price_info = product.get("priceInfo") or {}

        summary = price_info.get("summary") or {}

        return {

            "item_id": product.get("itemId"),

            "item_name": product.get("itemNm"),

            "site_no": product.get("siteNo"),

            "salestr_no": product.get("salestrNo"),

            "price": product.get("displayPrc"),

            "price_text": summary.get("priceTxt"),

            "sold_out": product.get("soldOutYn"),

            "stopped_selling": product.get("stoppedSellingYn"),

            "item_url": product.get("itemLnkd"),

            "image_url": product.get("itemImgUrl")

        }
 