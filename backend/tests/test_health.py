def test_health_check(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "OpenGovSA"
    assert data["version"] == "0.1.0"


def test_liveness_check(client):
    response = client.get("/api/v1/health/live")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "OpenGovSA"
    assert data["version"] == "0.1.0"


def test_readiness_check(client):
    response = client.get("/api/v1/health/ready")
    # Note: This test assumes database is available. In CI, the database service is started.
    # If database is unavailable, returns 503 with status "unavailable"
    assert response.status_code in [200, 503]
    data = response.json()
    assert data["service"] == "OpenGovSA"
    assert data["version"] == "0.1.0"
    if response.status_code == 200:
        assert data["status"] == "ok"
    else:
        assert data["status"] == "unavailable"
