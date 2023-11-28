class ExpectedResult:
    support_url = "https://reqres.in/#support-heading"
    support_message = "To keep ReqRes free, contributions towards server costs are appreciated!"
    data_keys = ["id", "email", "first_name", "last_name", "avatar"]
    keys_list_users = ["data", "page", "per_page", "support", "total", "total_pages"]


class CreateUserData:
    body_for_create_new_user = {
        "name": "neo",
        "job": "leader"}
    some_body_for_create_user = {
        "name": "neo",
        "job": "leader"}
