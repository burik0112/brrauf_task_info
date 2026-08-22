---
title: "Get the list of task results tasks.task.result.list | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/result/tasks-task-result-list.html"
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

The method `tasks.task.result.list` retrieves the list of results associated with a task.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the task from which to retrieve results.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/tasks-task-list.html) |

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
-d '{"taskId":8017}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.result.list
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":8017,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.result.list
```

```javascript
// callListMethod is recommended when you need to retrieve
// the entire set of list data and the volume of records is relatively small
// (up to about 1000 items). The method loads all data at once, which
// can lead to high memory load when working with large volumes.

try {
const response = await $b24.callListMethod(
    'tasks.task.result.list',
    { taskId: 8017 },
    (progress: number) => { console.log('Progress:', progress) }
);
const items = response.getData() || [];
for (const entity of items) { console.log('Entity:', entity) }
} catch (error: any) {
console.error('Request failed', error)
}

// fetchListMethod is preferable when working with large datasets.
// The method implements iterative sampling using a generator, which
// allows processing data in parts and efficiently using memory.

try {
const generator = $b24.fetchListMethod('tasks.task.result.list', { taskId: 8017 }, 'ID');
for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
}
} catch (error: any) {
console.error('Request failed', error)
}

// callMethod provides manual control over the pagination
// of data retrieval through the start parameter. Suitable for scenarios where
// precise control over request batches is required. However, with large
// volumes of data, it may be less efficient compared to
// fetchListMethod.

try {
const response = await $b24.callMethod('tasks.task.result.list', { taskId: 8017 }, 0);
const result = response.getData().result || [];
for (const entity of result) { console.log('Entity:', entity) }
} catch (error: any) {
console.error('Request failed', error)
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'tasks.task.result.list',
            [
                'taskId' => 8017
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error listing task results: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.result.list',
    {
        "taskId": 8017
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
    'tasks.task.result.list',
    [
        'taskId' => 8017
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
    "result": [
        {
            "id": 23,
            "taskId": 8017,
            "commentId": 3197,
            "createdBy": 503,
            "createdAt": "2025-07-15T14:30:00+02:00",
            "updatedAt": "2025-08-19T16:45:48+02:00",
            "status": 0,
            "text": "The client signed the documents",
            "formattedText": "The client signed the documents",
            "files": []
        },
        {
            "id": 21,
            "taskId": 8017,
            "commentId": 3199,
            "createdBy": 503,
            "createdAt": "2025-07-13T14:30:00+02:00",
            "updatedAt": "2025-08-19T16:45:56+02:00",
            "status": 0,
            "text": "Sent documents to the client. The client promises to respond on [B]Monday[\/B].",
            "formattedText": "Sent documents to the client. The client promises to respond on \u003Cb\u003EMonday\u003C\/b\u003E.",
            "files": [1055,1057,1059,1061,1063]
        }
    ],
    "time": {
        "start": 1755611166.509052,
        "finish": 1755611166.542696,
        "duration": 0.03364396095275879,
        "processing": 0.00906991958618164,
        "date_start": "2025-08-19T16:46:06+02:00",
        "date_finish": "2025-08-19T16:46:06+02:00",
        "operating_reset_at": 1755611766,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | An array of objects, where each object describes a task result |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the result |
| **taskId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the task |
| **commentId**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the comment marked as a result |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The identifier of the user who marked the result |
| **createdAt**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The date and time the result was marked in ISO 8601 format |
| **updatedAt**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The date and time of the last modification of the result in ISO 8601 format |
| **status**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The status of the result. Possible values:  - `0` — result is open - `1` — result is closed  The result becomes closed after the task is completed and retains this status after the task is resumed. Only new results in an unfinished task will be open.  A comment with an open result cannot be added again to the result. If the result is closed, adding is possible |
| **text**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The text of the result |
| **formattedText**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | The text of the result with formatting |
| **files**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html) | A list of file identifiers attached to the result.  Contains an empty array if there are no files in the comment |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/data-types.html#time) | Information about the time taken for the request |

HTTP status: **400**

```json
{
    "error":"100",
    "error_description":"Invalid value {value} to match with parameter {commentId}. Should be value of type int."
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | Access denied. | The user does not have access to the task or a task with such `ID` does not exist |
| `100` | Invalid value {value} to match with parameter {commentId}. Should be value of type int. | An invalid type value was passed in the `taskId` parameter. It should be of type `integer` |

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
- [Add Comment to Result tasks.task.result.addFromComment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-add-from-comment.html)
- [Remove Comment from Result tasks.task.result.deleteFromComment](https://apidocs.bitrix24.com/api-reference/tasks/result/api-reference/tasks/result/tasks-task-result-delete-from-comment.html)