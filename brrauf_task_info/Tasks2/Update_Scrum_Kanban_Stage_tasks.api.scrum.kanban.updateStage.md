---
title: "Update Scrum Kanban Stage tasks.api.scrum.kanban.updateStage | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-update-stage.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

This method changes the stage of the Scrum Kanban.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **stageId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Identifier of the stage. You can obtain the identifier using the method [tasks.api.scrum.kanban.getStages](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-get-stages.html) |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Fields corresponding to the available list of fields [tasks.api.scrum.kanban.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-get-fields.html) (detailed description provided [below](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-update-stage.html#parametr-fields)) |

### Parameter fields

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **sprintId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Identifier of the sprint. You can obtain the identifier using the method [tasks.api.scrum.sprint.list](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-list.html) |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Name of the kanban stage |
| **type**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Type of the kanban stage. Possible values: `NEW`, `WORK`, `FINISH` |
| **sort**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Sort order. The value of the field must be a multiple of `100` |
| **color**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/data-types.html) | Color of the kanban stage |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"stageId":65,"fields":{"name":"Updated Stage","type":"WORK","color":"00C4FB","sort":100}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.api.scrum.kanban.updateStage
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"stageId":65,"fields":{"name":"Updated Stage","type":"WORK","color":"00C4FB","sort":100},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.api.scrum.kanban.updateStage
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.kanban.updateStage',
            [
                'stageId' => 65,
                'fields'  => [
                    'name'  => 'Updated Stage',
                    'type'  => 'WORK',
                    'color' => '00C4FB',
                    'sort'  => 100,
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error updating stage: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.api.scrum.kanban.updateStage',
    {
        "stageId": 65,
        "fields": {
            "name": "Updated Stage",
            "type": "WORK",
            "color": "00C4FB",
            "sort": 100,
        },
    },
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
    'tasks.api.scrum.kanban.updateStage',
    [
        'stageId' => 65,
        'fields' => [
            'name' => 'Updated Stage',
            'type' => 'WORK',
            'sort' => 100,
            'color' => '00C4FB',
        ],
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

```json
{
    "result": true,
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

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Incorrect sprintId value"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | `Stage id not found` | Required field `stageId` is not filled |
| `0` | `Stage not found` | An unknown stage identifier `stageId` was provided |
| `0` | `Incorrect sprintId value` | An unknown sprint identifier was provided or no access to the sprint |
| `0` | `Access denied` | Access is denied |
| `0` | Unknown error |  |

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

- [Kanban in Scrum: Overview of Methods](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/index.html)
- [Create a Scrum Kanban Stage tasks.api.scrum.kanban.addStage](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-add-stage.html)
- [Add Task to Scrum Kanban tasks.api.scrum.kanban.addTask](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-add-task.html)
- [Delete Stage tasks.api.scrum.kanban.deleteStage](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-delete-stage.html)
- [Delete Task from Scrum Kanban tasks.api.scrum.kanban.deleteTask](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-delete-task.html)
- [Get a list of available fields for the kanban stage tasks.api.scrum.kanban.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-get-fields.html)
- [Get Kanban Stages by Sprint ID tasks.api.scrum.kanban.getStages](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/kanban/api-reference/sonet-group/scrum/kanban/tasks-api-scrum-kanban-get-stages.html)