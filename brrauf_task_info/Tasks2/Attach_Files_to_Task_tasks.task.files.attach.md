---
title: "Attach Files to Task tasks.task.files.attach | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-files-attach.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: task Creator or a user with edit access to the task

The method `tasks.task.files.attach` adds a file from Disk to a task. The user must have read access or higher to the file.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The identifier of the task to which the file needs to be attached.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [getting the list of tasks](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) method. |
| **fileId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The identifier of the file on Disk.  The file identifier can be obtained in two ways.  Use one of the file upload methods:  - [disk.storage.uploadfile](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/disk/storage/disk-storage-upload-file.html) - [disk.folder.uploadfile](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/disk/folder/disk-folder-upload-file.html)  Use one of the methods to get the list of files:  - [disk.storage.getchildren](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/disk/storage/disk-storage-get-children.html) - [disk.folder.getchildren](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/disk/folder/disk-folder-get-children.html) |

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
-d '{"taskId":8017,"fileId":1065}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.files.attach
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":8017,"fileId":1065,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.files.attach
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.files.attach',
        {
            taskId: 8017,
            fileId: 1065
        }
    );
    
    const result = response.getData().result;
    console.log('File attached:', result);
    
    processResult(result);
}
catch( error )
{
    console.error('Error:', error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.files.attach',
            [
                'taskId' => 8017,
                'fileId' => 1065
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error attaching file: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.files.attach',
    {
        taskId: 8017,
        fileId: 1065
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.files.attach',
    [
        'taskId' => 8017,
        'fileId' => 1065
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": {
        "attachmentId": 1079
    },
    "time": {
        "start": 1758806783,
        "finish": 1758806783.609955,
        "duration": 0.6099550724029541,
        "processing": 0,
        "date_start": "2025-09-25T16:26:23+02:00",
        "date_finish": "2025-09-25T16:26:23+02:00",
        "operating_reset_at": 1758807383,
        "operating": 0.4156019687652588
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The root element of the response. Contains an object with the description of the attached file |
| **attachmentId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | The identifier of the file attachment to the task.  Data about the file can be obtained by the attachment identifier using the [disk.attachedObject.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/disk/attached-object/disk-attached-object-get.html) method |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the execution time of the request |

HTTP Status: **400**

```json
{
    "error": "100",
    "error_description": "Could not find value for parameter {fileId} (internal error)"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `100` | CTaskItem All parameters in the constructor must have real class type (internal error) | Required parameter `taskId` is missing |
| `0` | wrong task id (internal error) | The value in the `taskId` parameter is of an incorrect type |
| `100` | Could not find value for parameter {fileId} (internal error) | Required parameter `fileId` is missing |
| `100` | Invalid value {value} to match with parameter {fileId}. Should be value of type int. (internal error) | The value in the `fileId` parameter is of an incorrect type |
| `ERROR_CORE` | Insufficient permissions.\\u003Cbr\\u003E | No access to the specified file |
| `0` | Access denied (internal error) | Insufficient permissions to modify the task |

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

- [How to Upload a File to a Task](https://apidocs.bitrix24.com/api-reference/tasks/tutorials/tasks/how-to-upload-file-to-task.html)
- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)