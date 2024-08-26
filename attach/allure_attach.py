import json
import logging
from json import JSONDecodeError

import allure
from allure_commons.types import AttachmentType
from requests import Response


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    if response.request.body:
        try:
            logging.info("INFO Request body: " + json.dumps(json.loads(response.request.body), indent=4))
        except json.JSONDecodeError:
            logging.info("INFO Request body: " + str(response.request.body))
    logging.info("Request headers: " + str(response.request.headers))
    logging.info("Response code " + str(response.status_code))
    logging.info("Response: " + response.text)


def response_attaching(response):
    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    try:
        body = response.request.body
        if isinstance(body, bytes):
            body = json.loads(body.decode('utf-8'))
        allure.attach(
            body=json.dumps(body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
    except JSONDecodeError as e:
        allure.attach(
            body=str(e),
            name="Response",
            attachment_type=AttachmentType.TEXT,
            extension="txt",
        )
