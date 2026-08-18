---
title: "Start Sprint tasks.api.scrum.sprint.start | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-start.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.api.scrum.sprint.start` initiates a sprint.

Only a planned sprint can be started.

When starting a sprint, the columns of the active sprint and Automation rules will be carried over from the previous completed sprint, if one exists.

Tasks will be added to the kanban of the active sprint. If there were completed tasks in the sprint at that moment, they will be moved to the backlog.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint identifier |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (oAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
"id": 2
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.api.scrum.sprint.start
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Authorization: YOUR_ACCESS_TOKEN" \
-d '{
"id": 2
}' \
https://your-domain.bitrix24.com/rest/tasks.api.scrum.sprint.start
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.api.scrum.sprint.start',
        {
            id: sprintId
        }
    );
    
    const result = response.getData().result;
    console.log(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```php
$sprintId = 2;

try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.sprint.start',
            [
                'id' => $sprintId
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error starting sprint: ' . $e->getMessage();
}
```

```js
const sprintId = 2;
BX24.callMethod(
    'tasks.api.scrum.sprint.start',
    {
        id: sprintId
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php'); // connecting CRest PHP SDK

// executing request to REST API
$result = CRest::call(
    'tasks.api.scrum.sprint.start',
    [
        'id' => 2,
    ]
);

// Processing response from Bitrix24
if (isset($result['error'])) {
    echo 'Error: '.$result['error_description'];
} else {
    print_r($result['result']);
}
```

## Response Handling

HTTP status: **200**

```json
{
    "result":
    {
        "id": 2,
        "groupId": 143,
        "entityType": "sprint",
        "name": "Sprint 1",
        "goal": "Sprint goal",
        "sort": 1,
        "createdBy": 1,
        "modifiedBy": 1,
        "dateStart": "2024-07-19T15:03:01+00:00",
        "dateEnd": "2024-08-02T15:03:01+00:00",
        "status": "active"
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Object containing sprint data |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint identifier |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Group identifier (Scrum) to which the sprint belongs |
| **entityType**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Entity type (in this case `sprint`) |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint name |
| **goal**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint goal. Set only in the interface when starting the sprint |
| **sort**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sorting |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Identifier of the user who created the sprint |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Identifier of the user who modified the sprint |
| **dateStart**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint start date in `ISO 8601` format |
| **dateEnd**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint end date in `ISO 8601` format |
| **status**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint status |

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Sprint not found"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Error Message** | **Description** |
| --- | --- | --- |
| `0` | `Access denied` | No access to Scrum |
| `0` | `Sprint not found` | Such a sprint does not exist |
| `0` | `Sprint must be planned` | Sprint must be in "planned" status |
| `100` | `Could not find value for parameter {id}` | Incorrect parameter name or parameter not set |
| `100` | `Invalid value {stringValue} to match with parameter {id}. Should be value of type int` | Invalid parameter type |

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

- [Add Sprint in Scrum tasks.api.scrum.sprint.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-add.html)
- [Update Sprint tasks.api.scrum.sprint.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-update.html)
- [Complete the active sprint of the selected Scrum tasks.api.scrum.sprint.complete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-complete.html)
- [Get Sprint Fields by Its Identifier tasks.api.scrum.sprint.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-get.html)
- [Get the list of sprints tasks.api.scrum.sprint.list](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-list.html)
- [Delete Sprint tasks.api.scrum.sprint.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-delete.html)
- [Get a list of available fields for the sprint tasks.api.scrum.sprint.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-get-fields.html)