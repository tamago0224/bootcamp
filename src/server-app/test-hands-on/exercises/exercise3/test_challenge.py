import unittest
from fastapi.testclient import TestClient
from . import challenge

client = TestClient(challenge.app)


class ApiTestCase(unittest.TestCase):
    # このテストは変更せず、テストが通るように "challenge.py" を改修してみましょう
    # 仕様通りにAPIを作成すると、このテストは成功するようになります
    def test_success(self):
        res = client.get("/")
        self.assertEqual(res.json(), {"current_number": 0})
        res = client.get("/add/123")
        self.assertEqual(res.json(), {"current_number": 123})
        res = client.get("/sub/13")
        self.assertEqual(res.json(), {"current_number": 110})
        res = client.get("/mul/5")
        self.assertEqual(res.json(), {"current_number": 550})
        res = client.get("/div/275")
        self.assertEqual(res.json(), {"current_number": 2})

        client.get("/sub/2")

    def test_tdd(self):
        # 値の取得のテスト。こちらは既に実装済みですのでテストは成功します
        res = client.get("/")
        data = res.json()
        self.assertEqual(data, {"current_number": 0})

        # 以下、加減乗除を行うAPIを作成するため、加算、減算、乗算、除算の順に動作をテストしてみましょう

        # サイクル(1) では、この加算のテストが通るように Red, Green, Refactoring をやってみましょう
        res = client.get("/add/10")
        data = res.json()
        self.assertEqual(data, {"current_number": 10})

        # 次に、サイクル(2) では、減算のテストを作り、Red, Green, Refactoring をやってみましょう

        # 続けて、サイクル (3) では乗算を完成させてみましょう

        # 最後に、サイクル (4) では除算を完成させてみましょう
