---
title: "Delegate a workflow task bizproc.task.delegate | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/bizproc-task-delegate.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`bizproc`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user responsible for the workflow task

This method delegates a workflow task. You can only delegate your own task.

User documentation

- [Actions: Tasks](https://helpdesk.bitrix24.com/open/11466058/)

## Method parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **TASK\_IDS** \*   [`array`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | List of task identifiers.  You can obtain identifiers using the [bizproc.task.list](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-list.html) method. |
| **FROM\_USER\_ID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Identifier of the user from whom the tasks will be delegated.  You can obtain the user identifier using the [user.get](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/user/user-get.html) method. |
| **TO\_USER\_ID** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Identifier of the user to whom the tasks will be delegated.  You can obtain the user identifier using the [user.get](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/user/user-get.html) method.  Who you can delegate to depends on the task settings: only subordinates, all employees, or no one. |

## Code examples

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
-d '{"TASK_IDS":[1128,1129,1130],"FROM_USER_ID":15,"TO_USER_ID":37}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/bizproc.task.delegate
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASK_IDS":[1128,1129,1130],"FROM_USER_ID":15,"TO_USER_ID":37,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/bizproc.task.delegate
```

```javascript
try
{
    const response = await $b24.callMethod(
        'bizproc.task.delegate',
        {
            TASK_IDS: [1128, 1129, 1130],
            FROM_USER_ID: 15,
            TO_USER_ID: 37,
        }
    );
    
    const result = response.getData().result;
    console.log('Delegated tasks:', result);
    
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
            'bizproc.task.delegate',
            [
                'TASK_IDS' => [1128, 1129, 1130],
                'FROM_USER_ID' => 15,
                'TO_USER_ID' => 37,
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error delegating task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'bizproc.task.delegate',
    {
        'TASK_IDS': [1128, 1129, 1130],
        'FROM_USER_ID': 15,
        'TO_USER_ID': 37,
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
    'bizproc.task.delegate',
    [
        'TASK_IDS' => [1128, 1129, 1130],
        'FROM_USER_ID' => 15,
        'TO_USER_ID' => 37
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
        "start": 1748526089.625516,
        "finish": 1748526089.656787,
        "duration": 0.03127098083496094,
        "processing": 0.008746147155761719,
        "date_start": "2025-05-29T16:41:29+02:00",
        "date_finish": "2025-05-29T16:41:29+02:00",
        "operating_reset_at": 1748526689,
        "operating": 0
    }
}
```

### Returned data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`boolean`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html) | Returns `true` if the task was successfully delegated. |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/data-types.html#time) | Information about the request execution time. |

HTTP status: **400**

```json
{
    "error": "ERROR_INVALID_USER_ID",
    "error_description": "Invalid FROM_USER_ID"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Error message** | **Description** |
| --- | --- | --- |
| `ERROR_TASK_VALIDATION` | Invalid TASK\_IDS | Invalid task identifiers or the `TASK_IDS` parameter was not provided. |
| `ERROR_INVALID_USER_ID` | Invalid FROM\_USER\_ID | Invalid or missing user identifier from whom the delegation is made. |
| `ERROR_INVALID_USER_ID` | Invalid TO\_USER\_ID | Invalid or missing user identifier to whom the delegation is made. |
| `ERROR_DELEGATION_NOT_ALLOWED` | User is not responsible for the task | The user specified in the `FROM_USER_ID` parameter is not responsible for the task. |
| `ERROR_DELEGATION_NOT_ALLOWED` | Task delegation is only available for intranet users | The user specified in the `TO_USER_ID` parameter is not an intranet user. |
| `ERROR_DELEGATION_NOT_ALLOWED` | List of errors separated by `;` | The method can accept multiple tasks. If errors occur in multiple tasks, they will be returned as a list separated by `;`. |

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

## Continue exploring

- [Workflow Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/index.html)
- [Get the list of workflow tasks bizproc.task.list](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-list.html)
- [Complete a business process task bizproc.task.complete](https://apidocs.bitrix24.com/api-reference/bizproc/bizproc-task/api-reference/bizproc/bizproc-task/bizproc-task-complete.html)