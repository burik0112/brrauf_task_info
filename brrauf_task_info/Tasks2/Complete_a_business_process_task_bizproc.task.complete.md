---
title: "Complete a business process task bizproc.task.complete | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/bizproc-task-complete.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`bizproc`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

This method completes a business process task:

- Document approval
- Document acknowledgment
- Request for additional information
- Request for additional information with rejection

You can only complete your own task.

User documentation

- [Actions: Tasks](https://helpdesk.bitrix24.com/open/11466058/)

## Method parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASK\_ID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Task identifier.  You can obtain the identifier using the [bizproc.task.list](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-list.html) method. |
| **STATUS** \*   [`integer` \| `string`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Target status of the task. Possible values:  - `1` or `yes` — yes, approved - `2` or `no` — no, rejected - `3` or `ok` — ok, acknowledged - `4` or `cancel` — cancellation  The set of acceptable values changes depending on the type of task:  - Document approval — `1` or `2` - Document acknowledgment — `3` - Request for additional information — `3` - Request for additional information with rejection — `3` or `4` |
| **COMMENT**   [`string`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | User comment.  The requirement for this parameter depends on the task settings. |
| **FIELDS**   [`object`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | An object describing fields for completing tasks with a request for additional information in the format `{"field_1": "value_1", ... "field_N": "value_N"}`, where  - `field_N` — symbolic identifier of the task field - `value_N` — value of the field  You can obtain field descriptions in the task using the [bizproc.task.list](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-list.html) method in the object `"PARAMETERS": "Fields"` of the response. The structure of the field object description:  ```json "PARAMETERS": {     ...     "Fields": [         {             "Id": "field_id",             "Type": "type",             "Name": "name",             "Description": "description",             "Multiple": false,             "Required": true,             "Options": null,             "Settings": null,             "Default": "default_value"         } ```  `Id` — symbolic identifier of the task field.  The `Default` contains default values that can be passed for task completion. These values are converted to an external representation:  - for dates — in the rest ATOM ISO-8601 format - for files — as a link to the file  Values are passed in this format to the `bizproc.task.complete` method. They are then converted to an internal representation:  - dates from the rest format are converted to internal format - files are saved and attached to the business process  To pass a value in a File type field, specify:  - for File type — base64 or an array with the name and base64 - for File type (Drive) — file identifier from Drive  More about working with files can be found in the article [How to Upload Files](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/files/how-to-upload-files.html) |

## Code example

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
-d '{"TASK_ID":1501,"STATUS":1,"COMMENT":"Added","Fields":{"contractor":"C_607","phone_number":"+19991234567"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/bizproc.task.complete
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASK_ID":1501,"STATUS":1,"COMMENT":"Added","Fields":{"contractor":"C_607","phone_number":"+19991234567"},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/bizproc.task.complete
```

```js
try
{
    const response = await $b24.callMethod(
        'bizproc.task.complete',
        {
            'TASK_ID': 1501,
            'STATUS': 1,
            'COMMENT': 'Added',
            "Fields": {
                'contractor': 'C_607',
                'phone_number': '+19991234567'
            }
        }
    );
    
    const result = response.getData().result;
    console.log(result);
}
catch( error )
{
    alert("Error: " + error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'bizproc.task.complete',
            [
                'TASK_ID' => 1501,
                'STATUS' => 1,
                'COMMENT' => 'Added',
                'Fields' => [
                    'contractor' => 'C_607',
                    'phone_number' => '+19991234567'
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        echo 'Error: ' . $result->error();
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error completing task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'bizproc.task.complete',
    {
        'TASK_ID': 1501,
        'STATUS': 1,
        'COMMENT': 'Added',
        "Fields": {
            'contractor': 'C_607',
            'phone_number': '+19991234567'
        }
    },
    function(result)
    {
        if(result.error())
            alert("Error: " + result.error());
        else
            console.log(result.data());
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'bizproc.task.complete',
    [
        'TASK_ID' => 1501,
        'STATUS' => 1,
        'COMMENT' => 'Added',
        'Fields' => [
            'contractor' => 'C_607',
            'phone_number' => '+19991234567'
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response handling

HTTP status: **200**

```json
{
    "result": true,
    "time": {
        "start": 1738746693.9218969,
        "finish": 1738746694.1367991,
        "duration": 0.21490216255187988,
        "processing": 0.19237995147705078,
        "date_start": "2025-02-05T12:11:33+01:00",
        "date_finish": "2025-02-05T12:11:34+01:00",
        "operating_reset_at": 1738747293,
        "operating": 0.19236207008361816
    }
}
```

### Returned data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Returns `true` if the task was completed successfully. |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html#time) | Information about the request execution time. |

HTTP status: **400**

```json
{
    "error": "ERROR_TASK_VALIDATION",
    "error_description": "incorrect STATUS"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Error message** | **Description** |
| --- | --- | --- |
| `ERROR_TASK_VALIDATION` | empty TASK\_ID | `ID` of the task is not specified. |
| `ERROR_TASK_VALIDATION` | incorrect STATUS | An incorrect task status is specified. |
| `ERROR_TASK_NOT_FOUND` | Task not found | No task found with the specified `ID`. |
| `ERROR_TASK_COMPLETED` | Task already completed | The task has already been completed. |
| `ERROR_TASK_TYPE` | Incorrect task type | Incorrect task type. This task cannot be completed via REST. |
| `ERROR_TASK_EXECUTION` | error text from the task | An error occurred during the execution of the task. |

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

## Continue learning

- [Workflow Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/index.html)
- [Get the list of workflow tasks bizproc.task.list](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-list.html)
- [Delegate a workflow task bizproc.task.delegate](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-delegate.html)