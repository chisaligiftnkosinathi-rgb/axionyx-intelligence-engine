# Deployment

The AXIONYX Intelligence Engine is designed for zero-configuration, reproducible deployment.

## Production (Railway)
AXIONYX uses **Railway** as its primary production orchestrator. The repository contains a `railway.toml` file at the root, which defines the exact build and runtime steps.

### Build Engine
Railway utilizes **Nixpacks** to automatically detect the Python environment via `requirements.txt`. Nixpacks builds a minimal, secure, and performant OCI container image without requiring a manual Dockerfile.

### `railway.toml` Configuration
```toml
[deploy]
  startCommand = "uvicorn src.app.main:app --host 0.0.0.0 --port $PORT"
  healthcheckPath = "/health"
  healthcheckTimeout = 10
```
*Note: Railway automatically injects the `$PORT` environment variable. The `startCommand` utilizes this to bind the Uvicorn ASGI server to the correct external port.*

## Local Development
To run the server locally:
1. Clone the repository.
2. Ensure you have Python 3.11+ installed.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn src.app.main:app --reload`
5. Navigate to `http://localhost:8000/docs` to view the interactive API.
