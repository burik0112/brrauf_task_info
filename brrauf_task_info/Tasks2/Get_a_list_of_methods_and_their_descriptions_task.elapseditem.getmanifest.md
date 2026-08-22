---
title: "Get a list of methods and their descriptions task.elapseditem.getmanifest | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/task-elapsed-item-get-manifest.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns a list of methods in the form of `task.elapseditem.*` and their descriptions.

The return value of this method is not intended for automated processing, as its format may change without notice.

The method can be useful as reference information, as it always contains up-to-date information.

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.elapseditem.getmanifest
```

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.elapseditem.getmanifest
```

```js
try
{
    const response = await $b24.callMethod(
        'task.elapseditem.getmanifest',
        {}
    );
    
    const result = response.getData().result;
    console.info(result);
}
catch( error )
{
    console.error(error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.elapseditem.getmanifest',
            []
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting manifest: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.elapseditem.getmanifest',
    {},
    function(result) {
        if (result.error()) {
            console.error(result.error());
        } else {
            console.info(result.data());
        }
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.elapseditem.getmanifest',
    []
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

```json
{
    "result": {
        "Manifest version": "1.2",
        "Manifest change date": "22 Feb 2018",
        "Warning": "Don't rely on the format of this manifest, it can be changed without any notifications!",
        "REST: shortname alias to class": "elapseditem",
        "REST: writable elapseditem data fields": [
            "USER_ID",
            "COMMENT_TEXT",
            "SECONDS",
            "SOURCE",
            "CREATED_DATE",
            "DATE_START",
            "DATE_STOP"
        ],
        "REST: readable elapseditem data fields": [
            "ID",
            "TASK_ID",
            "USER_ID",
            "COMMENT_TEXT",
            "SECONDS",
            "MINUTES",
            "SOURCE",
            "CREATED_DATE",
            "DATE_START",
            "DATE_STOP"
        ],
        "REST: sortable elapseditem data fields": [
            "ID",
            "TASK_ID",
            "USER_ID",
            "SECONDS",
            "MINUTES",
            "CREATED_DATE",
            "DATE_START",
            "DATE_STOP"
        ],
        "REST: filterable elapseditem data fields": [
            "ID",
            "TASK_ID",
            "USER_ID",
            "CREATED_DATE"
        ],
        "REST: date fields": [
            "CREATED_DATE",
            "DATE_START",
            "DATE_STOP"
        ],
        "REST: available methods": {
            "getmanifest": {
                "staticMethod": true,
                "params": []
            },
            "getlist": {
                "staticMethod": true,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "order",
                        "type": "array",
                        "allowedKeys": [
                            "ID",
                            "TASK_ID",
                            "USER_ID",
                            "SECONDS",
                            "MINUTES",
                            "CREATED_DATE",
                            "DATE_START",
                            "DATE_STOP"
                        ]
                    },
                    {
                        "description": "filter",
                        "type": "array",
                        "allowedKeys": [
                            "ID",
                            "TASK_ID",
                            "USER_ID",
                            "CREATED_DATE"
                        ],
                        "allowedKeyPrefixes": [
                            "!",
                            "<=",
                            "<",
                            ">=",
                            ">"
                        ]
                    },
                    {
                        "description": "select",
                        "type": "array",
                        "allowedValues": [
                            "",
                            "*",
                            "ID",
                            "TASK_ID",
                            "USER_ID",
                            "COMMENT_TEXT",
                            "SECONDS",
                            "MINUTES",
                            "SOURCE",
                            "CREATED_DATE",
                            "DATE_START",
                            "DATE_STOP"
                        ],
                        "allowedAggregations": [
                            "MAX",
                            "MIN",
                            "COUNT",
                            "SUM",
                            "AVG"
                        ],
                        "allowedValuesInAggregation": [
                            "ID",
                            "USER_ID",
                            "SECONDS",
                            "MINUTES"
                        ]
                    },
                    {
                        "description": "params",
                        "type": "array",
                        "allowedKeys": [
                            "NAV_PARAMS"
                        ]
                    }
                ],
                "allowedKeysInReturnValue": [
                    "ID",
                    "TASK_ID",
                    "USER_ID",
                    "COMMENT_TEXT",
                    "SECONDS",
                    "MINUTES",
                    "SOURCE",
                    "CREATED_DATE",
                    "DATE_START",
                    "DATE_STOP"
                ],
                "allowedAggregations": [
                    "MAX",
                    "MIN",
                    "COUNT",
                    "SUM",
                    "AVG"
                ],
                "collectionInReturnValue": true
            },
            "get": {
                "mandatoryParamsCount": 2,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "itemId",
                        "type": "integer"
                    }
                ],
                "allowedKeysInReturnValue": [
                    "ID",
                    "TASK_ID",
                    "USER_ID",
                    "COMMENT_TEXT",
                    "SECONDS",
                    "MINUTES",
                    "SOURCE",
                    "CREATED_DATE",
                    "DATE_START",
                    "DATE_STOP"
                ]
            },
            "add": {
                "staticMethod": true,
                "mandatoryParamsCount": 2,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "fields",
                        "type": "array",
                        "allowedKeys": [
                            "USER_ID",
                            "COMMENT_TEXT",
                            "SECONDS",
                            "SOURCE",
                            "CREATED_DATE",
                            "DATE_START",
                            "DATE_STOP"
                        ]
                    }
                ]
            },
            "update": {
                "staticMethod": false,
                "mandatoryParamsCount": 3,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "itemId",
                        "type": "integer"
                    },
                    {
                        "description": "fields",
                        "type": "array",
                        "allowedKeys": [
                            "USER_ID",
                            "COMMENT_TEXT",
                            "SECONDS",
                            "SOURCE",
                            "CREATED_DATE",
                            "DATE_START",
                            "DATE_STOP"
                        ]
                    }
                ]
            },
            "delete": {
                "staticMethod": false,
                "mandatoryParamsCount": 2,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "itemId",
                        "type": "integer"
                    }
                ]
            },
            "isactionallowed": {
                "staticMethod": false,
                "mandatoryParamsCount": 3,
                "params": [
                    {
                        "description": "taskId",
                        "type": "integer"
                    },
                    {
                        "description": "itemId",
                        "type": "integer"
                    },
                    {
                        "description": "actionId",
                        "type": "integer"
                    }
                ]
            }
        }
    },
    "time": {
        "start": 1712137817.343984,
        "finish": 1712137817.605804,
        "duration": 0.26182007789611816,
        "processing": 0.018325090408325195,
        "date_start": "2024-04-03T12:50:17+02:00",
        "date_finish": "2024-04-03T12:50:17+02:00"
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Description of methods `task.elapseditem.*` |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Information about the request execution time |

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue Learning

- [Time Tracking in Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/index.html)
- [Add Time Entry task.elapseditem.add](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-add.html)
- [Update Time Entry task.elapseditem.update](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-update.html)
- [Get elapsed time record by identifier task.elapseditem.get](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get.html)
- [Get a list of time spent records task.elapseditem.getlist](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get-list.html)
- [Delete Time Entry task.elapseditem.delete](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-delete.html)
- [Check Action Permission for task.elapseditem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-is-action-allowed.html)