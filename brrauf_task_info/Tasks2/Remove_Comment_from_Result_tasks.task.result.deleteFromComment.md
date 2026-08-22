---
title: "Remove Comment from Result tasks.task.result.deleteFromComment | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/result/tasks-task-result-delete-from-comment.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user with access to the task

The method `tasks.task.result.deleteFromComment` removes the pinning of a comment as the result of a task. To delete a comment from the result, use the method [task.commentitem.delete](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/comment-item/task-comment-item-delete.html).

A user can only unpin their own comment. An administrator can unpin any user's comment.

When working with the [new task detail form](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/tasks-new.html) with chat from version `tasks 25.700.0`, the method does not work.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **commentId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the comment for which the result needs to be unpinned.  The comment identifier can be obtained when [adding a new comment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/comment-item/task-comment-item-add.html) or by using the [method to get the list of comments](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/comment-item/task-comment-item-get-list.html) for the task |

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
-d '{"commentId":3199}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.result.deleteFromComment
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"commentId":3199,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.result.deleteFromComment
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.result.deleteFromComment',
        {
            commentId: 3199,
        }
    );
    
    const result = response.getData().result;
    console.log('Deleted comment with ID:', result);
    
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
            'tasks.task.result.deleteFromComment',
            [
                'commentId' => 3199
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deleting comment: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.result.deleteFromComment',
    {
        "commentId": 3199
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
    'tasks.task.result.deleteFromComment',
    [
        'commentId' => 3199
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
    "result": null,
    "time": {
        "start": 1755611282.263157,
        "finish": 1755611282.322503,
        "duration": 0.05934619903564453,
        "processing": 0.031157970428466797,
        "date_start": "2025-08-19T16:48:02+02:00",
        "date_finish": "2025-08-19T16:48:02+02:00",
        "operating_reset_at": 1755611882,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   `null` | Returns `null` in case of successful execution |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html#time) | Information about the execution time of the request |

HTTP status: **400**

```json
{
    "error":"ERROR_CORE",
    "error_description":"TASKS_ERROR_EXCEPTION_#4; Action is not allowed; 4/TE/ACTION_NOT_ALLOWED.<br>"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Access denied. | The user does not have access permission to the task or the comment does not belong to the user |
| `100` | Invalid value {value} to match with parameter {commentId}. Should be value of type int. | The parameter `commentId` has an invalid type. It should be of type `integer` |
| `0` | Comment not found. | A comment with such an identifier does not exist |

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

- [Task Results: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/index.html)
- [Get the list of task results tasks.task.result.list](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-list.html)
- [Add Comment to Result tasks.task.result.addFromComment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-add-from-comment.html)