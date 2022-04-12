### What?!
Trying to implement (some of) this api-calls with fastapi:
<https://github.com/OCR-D/spec/blob/master/openapi.yml>

### Templates for api-calls
`../ocrd_openapi_to_fastapi`

### Start Dev-Server
`uvicorn ocrd_webapi_test.main:app --host 0.0.0.0 --reload`

### POST-request with Curl:
`curl -X POST http://localhost:8000/workspace -H 'content-type: multipart/form-data' -F
 file=@stuff/example_ws.ocrd.zip`
