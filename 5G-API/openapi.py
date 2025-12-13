import json
import logging
import sys 
import pathlib
import yaml
logging.basicConfig(
    level=logging.INFO,
    format="level=%(levelname)s file=%(filename)s line=%(lineno)d message=%(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

HTTP_METHODS = {"get", "post", "put", "delete", "patch"}

class APIResponseError(Exception):
    pass

def get_effective_security(spec, method_details):
    if "security" in method_details:
        return method_details["security"]
    return spec.get("security", [])

def parse_openapi_file(file_path):
    logger.info("Parsing file=%s", file_path)

    try:
        with open(file_path, encoding="utf-8") as f:
                      spec = yaml.safe_load(f)
    except Exception as e:
        logger.error("Failed to load YAML: %s error=%s", file_path, e)
        raise APIResponseError(f"Invalid YAML: {file_path}")

    info = spec.get("info", {})
    paths = spec.get("paths", {})

    if not isinstance(paths, dict):
        logger.error("Missing or invalid 'paths' section in %s", file_path)
        raise APIResponseError("paths missing")
    
   
    endpoint = []
    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
    for method, details in path_item.items():
            m = method.lower()
            if m not in HTTP_METHODS:
                continue
            if not isinstance(details, dict):
                continue

            responses = details.get("responses", {}) or {}

            has_body = any(
                isinstance(r, dict) and "content" in r for r in responses.values()
            )
            endpoint.append(
                 {
                    "path": path,
                    "method": m.upper(),
                    "operationId": details.get("operationId"),
                    "status_codes": list(responses.keys()),
                    "has_response_body": has_body,
                 }
            )
    return {
        "file": (file_path).name,
        "title": info.get("title"),
        "version": info.get("version"),
        "endpoints": endpoint,
    }

