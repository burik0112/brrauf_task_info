---
title: "Get the list of tasks from the Planner for the day task.planner.getlist | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/planner/task-planner-get-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/planner/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `task.planner.getlist` retrieves a list of task identifiers from the "Planner for the day" of the current user. To get detailed information about the tasks, use the method [tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/planner/api-reference/tasks/tasks-task-get.html).

## Method Parameters

No parameters.

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (OAuth)

JS

PHP

BX24.js

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.planner.getlist
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.planner.getlist
```

```javascript
// callListMethod is recommended when you need to retrieve
// the entire set of list data and the volume of records is relatively small
// (up to about 1000 items). The method loads all data at once, which
// can lead to high memory load when working with large volumes.

try {
    const response = await $b24.callListMethod(
    "task.planner.getlist",
    {},
    (progress) => {
        console.log("Progress:", progress);
    }
    );
    const items = response.getData() || [];
    for (const entity of items) {
    console.log("Entity:", entity);
    }
} catch (error) {
    console.error("Request failed", error);
}

// fetchListMethod is preferable when working with large datasets.
// The method implements iterative selection using a generator, which
// allows processing data in parts and efficiently using memory.

try {
    const generator = $b24.fetchListMethod("task.planner.getlist", {}, "ID");
    for await (const page of generator) {
    for (const entity of page) {
        console.log("Entity:", entity);
    }
    }
} catch (error) {
    console.error("Request failed", error);
}

// callMethod provides manual control over the pagination
// data retrieval process through the start parameter. It is suitable for scenarios where
// precise control over request batches is required. However, with large
// volumes of data, it may be less efficient compared to
// fetchListMethod.

try {
    const response = await $b24.callMethod("task.planner.getlist", {}, 0);
    const result = response.getData().result || [];
    for (const entity of result) {
    console.log("Entity:", entity);
    }
} catch (error) {
    console.error("Request failed", error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.planner.getlist',
            []
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error fetching task planner list: ' . $e->getMessage();
}
```

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

try {
  const response = await $b24.callListMethod(
    'task.planner.getlist',
    {},
    (progress) => { console.log('Progress:', progress) }
  )
  const items = response.getData() || []
  for (const entity of items) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}

// fetchListMethod is preferable when working with large datasets. The method implements iterative selection using a generator, which allows processing data in parts and efficiently using memory.

try {
  const generator = $b24.fetchListMethod('task.planner.getlist', {}, 'ID')
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
  }
} catch (error) {
  console.error('Request failed', error)
}

// callMethod provides manual control over the pagination data retrieval process through the start parameter. It is suitable for scenarios where precise control over request batches is required. However, with large volumes of data, it may be less efficient compared to fetchListMethod.

try {
  const response = await $b24.callMethod('task.planner.getlist', {}, 0)
  const result = response.getData().result || []
  for (const entity of result) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.planner.getlist',
            []
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result->data(), true);
    echo 'Full Result: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting task planner list: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    "task.planner.getlist",
    [],
    function (result) {
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.planner.getlist',
    []
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP Status: **200**

```json
{
    "result": [7811, 8017, 7789, 8015],
    "time": {
        "start": 1755252195.609436,
        "finish": 1755252195.636649,
        "duration": 0.027212858200073242,
        "processing": 0.0030121803283691406,
        "date_start": "2025-08-15T13:03:15+02:00",
        "date_finish": "2025-08-15T13:03:15+02:00",
        "operating_reset_at": 1755252795,
        "operating": 0
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/planner/api-reference/data-types.html) | List of task identifiers.  If there are no tasks in the planner for the day, it returns an empty array |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/planner/api-reference/data-types.html#time) | Information about the request execution time |

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

- [Tasks in "Planner": Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/planner/api-reference/tasks/planner/index.html)