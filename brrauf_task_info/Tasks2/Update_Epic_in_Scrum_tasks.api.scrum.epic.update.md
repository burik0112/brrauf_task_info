---
title: "Update Epic in Scrum tasks.api.scrum.epic.update | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-update.html"
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

This method updates an epic in Scrum.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **id** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic identifier.  You can obtain epic identifiers using the [`tasks.api.scrum.epic.list`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-list.html) method. |
| **fields** \*   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Field values (detailed description provided [below](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-update.html#parametr-fields)) for adding a new epic in the form of a structure:  ```js fields: {     name: 'value',     groupId: 'value',     description: 'value',     color: 'value',     files: [         'file1',         'file2',         ...     ]  } ``` |

### Parameter fields

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **name** \*   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic name |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic description |
| **groupId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Group identifier (Scrum) to which the epic belongs |
| **color**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic color |
| **files**   [`array`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Array of files associated with the epic.  In `files`, you can pass an array of values with file identifiers, specifying the prefix `n` for each identifier.  Attention  If you pass an empty array, the files will be deleted. |

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
-d '{
"fields": {
    "id": 1,
    "fields": {
        "name": "Updated epic name",
        "description": "Updated description text",
        "color": "#bbecf1",
        "files": ["n429", "n243"]
    }
},
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.api.scrum.epic.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
"fields": {
    "id": 1,
    "fields": {
        "name": "Updated epic name",
        "description": "Updated description text",
        "color": "#bbecf1",
        "files": ["n429", "n243"]
    }
},
auth=YOUR_ACCESS_TOKEN
}' \
https://your-domain.bitrix24.com/rest/tasks.api.scrum.epic.update
```

```js
try
{
    const response = await $b24.callMethod(
        'tasks.api.scrum.epic.update',
        {
            id: epicId,
            fields:{
                name: name,
                description: description,
                color: color,
                files: files
            }
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
    $name = 'Updated epic name';
    $description = 'Updated description text';
    $color = '#bbecf1';
    $files = ['n429', 'n243'];

    $response = $b24Service
        ->core
        ->call(
            'tasks.api.scrum.epic.update',
            [
                'id' => $epicId,
                'fields' => [
                    'name' => $name,
                    'description' => $description,
                    'color' => $color,
                    'files' => $files
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error updating epic: ' . $e->getMessage();
}
```

```js
const epicId = 1;
const name = 'Updated epic name';
const description = 'Updated description text';
const color = '#bbecf1';
const files = ['n429', 'n243'];
BX24.callMethod(
    'tasks.api.scrum.epic.update',
    {
        id: epicId,
        fields:{
            name: name,
            description: description,
            color: color,
            files: files
        }
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php'); // connecting CRest PHP SDK
$epicId = 1;
$name = 'Updated epic name';
$description = 'Updated description text';
$color = '#bbecf1';
$files = ['n429', 'n243'];

// executing request to REST API
$result = CRest::call(
'tasks.api.scrum.epic.update',
[
    'id' => $epicId,
    'fields' => [
        'name' => $name,
        'description' => $description,
        'color' => $color,
        'files' => $files
    ]
]
);

// Processing the response from Bitrix24
if ($result['error']) {
    echo 'Error: '.$result['error_description'];
}
else {
    print_r($result['result']);
}
```

## Response Handling

HTTP Status: **200**

```json
{
    "id": 1,
    "groupId": 143,
    "name": "Updated epic name",
    "description": "Updated description text",
    "createdBy": 1,
    "modifiedBy": 1,
    "color": "#bbecf1"
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic identifier |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Group identifier (Scrum) to which the epic is linked |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic name |
| **description**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic description |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who created the epic |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Identifier of the user who last modified the epic |
| **color**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/data-types.html) | Epic color |

HTTP Status: **400**

```json
{
    "error": 0,
    "error_description": "Epic not updated"
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
| `0` | Epic not updated | Failed to update the epic |
| `0` | createdBy user not found | User in the "creator" field not found |
| `0` | modifiedBy user not found | User in the "last modified by" field not found |
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
- [Get Epic Fields by Its Identifier tasks.api.scrum.epic.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get.html)
- [Get a list of epics tasks.api.scrum.epic.list](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-list.html)
- [Delete Epic tasks.api.scrum.epic.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-delete.html)
- [Get a list of available fields for epic tasks.api.scrum.epic.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/epic/api-reference/sonet-group/scrum/epic/tasks-api-scrum-epic-get-fields.html)