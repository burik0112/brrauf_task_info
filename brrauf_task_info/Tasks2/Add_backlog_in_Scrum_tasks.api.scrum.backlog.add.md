---
title: "Add backlog in Scrum tasks.api.scrum.backlog.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/tasks-api-scrum-backlog-add.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.api.scrum.backlog.add` adds a backlog in Scrum.

It may be necessary to create a backlog during import after creating the Scrum.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **fields** \*   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | An object containing records about the group and user (detailed description provided below) in the following structure:  ```js "fields": {     "groupId": value,     "createdBy": value,     "modifiedBy": value, } ``` |

### Parameter fields

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **groupId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the group for which the backlog is created.  The group identifier can be obtained when creating a new group [sonet\_group.create](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/sonet-group-create.html) or when retrieving a list of existing groups [socialnetwork-api-workgroup-list.md](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/socialnetwork-api-workgroup-list.html) |
| **createdBy** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the user who will create the backlog |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the user who will modify the backlog |

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
-d '{"fields": {"groupId": 1, "createdBy": 1}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.api.scrum.backlog.add
```

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields": {"groupId": 1, "createdBy": 1}, "auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.api.scrum.backlog.add
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.api.scrum.backlog.add',
        {
            "fields": {
                "groupId": 125,
                "createdBy": 6,
            },
        }
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
            'tasks.api.scrum.backlog.add',
            [
                'fields' => [
                    'groupId'   => 125,
                    'createdBy' => 6,
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
        echo 'Error: ' . $result->error();
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error adding backlog: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.api.scrum.backlog.add',{
        "fields": {
            "groupId": 125,
            "createdBy": 6,
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
'tasks.api.scrum.backlog.add',
    [
        'fields' => [
            'groupId' => 1,
            'createdBy' => 1,
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
    "result": {
        "id": 1,
        "groupId": 125,
        "createdBy": 6,
        "modifiedBy": 0
    },
    "time":{
        "start":1712137817.343984,
        "finish":1712137817.605804,
        "duration":0.26182007789611816,
        "processing":0.018325090408325195,
        "date_start":"2024-04-03T12:50:17+02:00",
        "date_finish":"2024-04-03T12:50:17+02:00"
    }
}
```

## Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the backlog |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the group for which the backlog was created |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the user who created the backlog |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/data-types.html) | The identifier of the user who modified the backlog |

HTTP status: **400**

```json
{
    "error":0,
    "error_description":"Access denied"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Error Message** | **Description** |
| --- | --- | --- |
| `0` | Backlog already added | The error occurs when trying to create a backlog while an active backlog already exists in the group |
| `0` | Access denied | Missing appropriate access permissions |
| `0` | createdBy user not found | The provided user identifier is invalid. For example, a user with such an identifier does not exist |
| `0` | modifiedBy user not found | The provided user identifier is invalid. For example, a user with such an identifier does not exist |
| `0` | Unknown error | Another error |

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

- [Update backlog tasks.api.scrum.backlog.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/scrum/backlog/tasks-api-scrum-backlog-update.html)
- [Get Backlog Fields by Scrum ID tasks.api.scrum.backlog.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/scrum/backlog/tasks-api-scrum-backlog-get.html)
- [Delete backlog tasks.api.scrum.backlog.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/scrum/backlog/tasks-api-scrum-backlog-delete.html)
- [Get a list of available backlog fields tasks.api.scrum.backlog.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/backlog/api-reference/sonet-group/scrum/backlog/tasks-api-scrum-backlog-get-fields.html)