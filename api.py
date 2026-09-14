def test_api(page):
    respponse = page.request.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert respponse.status == 200
    # data = respponse.json()
    # assert data["id"]== 1
    # assert "title" in data 

