class ResponseValidator:

    @staticmethod

    def validate_status_code(response, expected_status=200):

        actual_status = response.status_code

        assert actual_status == expected_status, (

            f"HTTP 상태 코드 불일치: "

            f"기대값={expected_status}, 실제값={actual_status}"

        )

    @staticmethod

    def validate_response_code(response_data, expected_code="200"):

        actual_code = response_data.get("res_code")

        assert str(actual_code) == str(expected_code), (

            f"API 응답 코드 불일치: "

            f"기대값={expected_code}, 실제값={actual_code}"

        )

    @staticmethod

    def validate_products(products):

        assert isinstance(products, list), (

            "상품 응답이 리스트 형식이 아닙니다."

        )

        assert len(products) > 0, (

            "검색된 상품이 없습니다."

        )

    @staticmethod

    def validate_product_fields(product):

        required_fields = [

            "item_id",

            "item_name",

            "price",

            "sold_out"

        ]

        for field in required_fields:

            assert product.get(field) is not None, (

                f"필수 상품 정보 누락: {field}"

            )

    @staticmethod

    def validate_search_keyword(products, keyword):

        matched_products = [

            product for product in products

            if keyword in product.get("item_name", "")

        ]

        assert matched_products, (

            f"검색어와 일치하는 상품이 없습니다: {keyword}"

        )
 