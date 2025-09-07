def test_health_endpoint(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    data = resp.json()
    assert data.get('status') == 'ok'
    assert 'Assistant container is running' in data.get('message', '')
