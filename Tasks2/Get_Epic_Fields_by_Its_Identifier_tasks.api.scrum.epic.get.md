---
title: "Get Epic Fields by Its Identifier tasks.api.scrum.epic.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with access to Scrum

The method retrieves the values of the epic fields by its identifier `id`.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic identifier.  You can get the identifiers of epics using the method [`tasks.api.scrum.epic.list`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-list.html) |

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
-d '{"id":1}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.api.scrum.epic.get
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"id":1,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.api.scrum.epic.get
```

```js
try
{
    const epicId = 1;
    const response = await $b24.callMethod(
        'tasks.api.scrum.epic.get',
        {
            id: epicId,
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
try {
    $epicId = 1;
    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.epic.get',
            [
                'id' => $epicId,
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting epic: ' . $e->getMessage();
}
```

```js
const epicId = 1;
BX24.callMethod(
    'tasks.api.scrum.epic.get',
    {
        id: epicId,
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.api.scrum.epic.get',
    [
        'id' => 1
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
    "id": 1,
    "groupId": 143,
    "name": "epic",
    "description": "",
    "createdBy": 1,
    "modifiedBy": 0,
    "color": "#69dafc",
    "files": {
        "ID": "136",
        "ENTITY_ID": "TASKS_SCRUM_EPIC",
        "FIELD_NAME": "UF_SCRUM_EPIC_FILES",
        "USER_TYPE_ID": "disk_file",
        "XML_ID": null,
        "SORT": "100",
        "MULTIPLE": "Y",
        "MANDATORY": "N",
        "SHOW_FILTER": "N",
        "SHOW_IN_LIST": "N",
        "EDIT_IN_LIST": "N",
        "IS_SEARCHABLE": "N",
        "SETTINGS": {
            "IBLOCK_ID": null,
            "SECTION_ID": null,
            "UF_TO_SAVE_ALLOW_EDIT": false
        },
        "USER_TYPE": {
            "USER_TYPE_ID": "disk_file",
            "CLASS_NAME": "Bitrix\\Disk\\Uf\\FileUserType",
            "DESCRIPTION": "File (Drive)",
            "BASE_TYPE": "int",
            "TAG": [
                "DISK FILE ID",
                "DOCUMENT ID"
            ]
        },
        "VALUE": [],
        "ENTITY_VALUE_ID": 1,
        "CUSTOM_DATA": {
            "PHOTO_TEMPLATE": ""
        },
        "EDIT_FORM_LABEL": "UF_SCRUM_EPIC_FILES",
        "TAG": "DOCUMENT ID"
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic identifier |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Group identifier (scrum) to which the epic is attached |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic name |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic description |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who created the epic |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who last modified the epic |
| **color**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic color in HEX format |
| **files**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Object with data about all files attached to the epic |

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Access denied"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Access denied | No access to view epic data |
| `0` | Epic not found | The epic does not exist |
| `100` | Could not find value for parameter | Incorrect parameter name or parameter not set |
| `100` | Invalid value {stringValue} to match with parameter {id}. Should be value of type int. | Invalid parameter type |

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

- [Epics in Scrum: Overview of Methods](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/index.html)
- [Add Epic in Scrum tasks.api.scrum.epic.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-add.html)
- [Update Epic in Scrum tasks.api.scrum.epic.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-update.html)
- [Get a list of epics tasks.api.scrum.epic.list](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-list.html)
- [Delete Epic tasks.api.scrum.epic.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-delete.html)
- [Get a list of available fields for epic tasks.api.scrum.epic.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get-fields.html)