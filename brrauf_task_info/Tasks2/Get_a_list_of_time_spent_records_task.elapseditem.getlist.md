---
title: "Get a list of time spent records task.elapseditem.getlist | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/task-elapsed-item-get-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns a list of time spent records for a task.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/tasks-task-list.html) |
| **ORDER**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Object for sorting the result (detailed description provided below) |
| **FILTER**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Object for filtering the result (detailed description provided below) |
| **SELECT**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Array of fields of records that will be returned by the method. You can specify only the fields that are necessary. If the array contains the value `"*"`, all available fields will be returned.  By default, all fields of the main query table will be returned |
| **PARAMS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Object for call options. The element is an object `NAV_PARAMS` of the form `{'call option': 'value' [, ...]}` (detailed description provided below) in the structure |

Warning

It is mandatory to follow the order of parameters specified in the table in the request. Otherwise, the request will execute with errors.

Note

Features of manually adding information about work time that was actually performed several days ago. In this case, the values of some fields change:

- `CREATED_DATE` — start date
- `DATE_START` — record creation date
- `DATE_STOP` — record end date

### ORDER Parameter

| **Name**   `type` | **Description** |
| --- | --- |
| **ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Identifier of the time spent record. Can take values:  - `asc` — ascending - `desc` — descending |
| **USER\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Identifier of the user on behalf of whom the time spent record was made. Can take values:  - `asc` — ascending - `desc` — descending |
| **MINUTES**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Time spent, in minutes. Can take values:  - `asc` — ascending - `desc` — descending |
| **SECONDS**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Time spent, in seconds. Can take values:  - `asc` — ascending - `desc` — descending |
| **CREATED\_DATE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Record creation date. Can take values:  - `asc` — ascending - `desc` — descending |
| **DATE\_START**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Start date. Can take values:  - `asc` — ascending - `desc` — descending |
| **DATE\_STOP**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | End date. Can take values:  - `asc` — ascending - `desc` — descending |

### FILTER Parameter

| **Name**   `type` | **Description** |
| --- | --- |
| **ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Identifier of the time spent record |
| **USER\_ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Identifier of the user on behalf of whom the time spent record was made |
| **CREATED\_DATE**   [`datetime`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Record creation date |

Note

Before the name of the filtered field, you can specify the type of filtering:

- "!" — not equal
- "<" — less than
- "<=" — less than or equal to
- ">" — greater than
- ">=" — greater than or equal to

*'filter values'* — single value or array

| **Name**   `type` | **Description** |
| --- | --- |
| **nPageSize**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Number of items per page. To limit the load on pagination, a limit of 50 records is imposed |
| **iNumPage**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Page number in pagination |

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
-d '[{"ID": "desc"},{">=CREATED_DATE": "2024-02-16"}]' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.elapseditem.getlist
```

```
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{[{"ID": "desc"},{">=CREATED_DATE": "2024-02-16"}],"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.elapseditem.getlist
```

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

try {
  const response = await $b24.callListMethod(
    'task.elapseditem.getlist',
    [
      1, 
      {'ID': 'desc'},
      {'<ID': 50}
    ],
    (progress) => { console.log('Progress:', progress) }
  )
  const items = response.getData() || []
  for (const entity of items) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}

// fetchListMethod is preferable when working with large datasets. The method implements iterative selection using a generator, allowing data to be processed in parts and efficiently using memory.

try {
  const generator = $b24.fetchListMethod('task.elapseditem.getlist', [{'ID': 'desc'}, {'>=CREATED_DATE': '2024-02-16'}, ['ID', 'TASK_ID'], {"NAV_PARAMS":{"nPageSize":2}}], 'ID')
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
  }
} catch (error) {
  console.error('Request failed', error)
}

// callMethod provides manual control over the pagination process through the start parameter. Suitable for scenarios where precise control over request batches is required. However, with large volumes of data, it may be less efficient compared to fetchListMethod.

try {
  const response = await $b24.callMethod('task.elapseditem.getlist', [{'ID': 'desc'}, {'>=CREATED_DATE': '2024-02-16'}, ['ID', 'TASK_ID'], {"NAV_PARAMS":{"nPageSize":2}}], 0)
  const result = response.getData().result || []
  for (const entity of result) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}
```

```php
try {
    // Get all time spent records sorted by ID in descending order.
    // Only records with ID less than 50 will be filtered.
    $response1 = $b24Service
        ->core
        ->call(
            'task.elapseditem.getlist',
            [
                1,
                ['ID' => 'desc'],
                ['<ID' => 50],
            ]
        );

    $result1 = $response1
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result1, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting elapsed time records: ' . $e->getMessage();
}

try {
    // Retrieve a sample of time spent based on general filtering conditions. For example, select data on labor costs from a specified date:
    $response2 = $b24Service
        ->core
        ->call(
            'task.elapseditem.getlist',
            [
                ['ID' => 'desc'],
                ['>=CREATED_DATE' => '2024-02-16'],
                ['ID', 'TASK_ID'],
                [
                    'NAV_PARAMS' => [
                        'nPageSize' => 2,
                    ],
                ],
            ]
        );

    $result2 = $response2
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result2, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting elapsed time records: ' . $e->getMessage();
}
```

## Response Handling

HTTP status: **200**

```json
{
    "result":[
        {
            "ID": "1",
            "TASK_ID": "691",
            "USER_ID": "1",
            "COMMENT_TEXT": "1",
            "SECONDS": "3600",
            "MINUTES": "60",
            "SOURCE": "2",
            "CREATED_DATE": "2024-05-16T10:33:00+02:00",
            "DATE_START": "2024-05-16T10:33:15+02:00",
            "DATE_STOP": "2024-05-16T10:33:15+02:00"
        }
    ],
    "total": 1,
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

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Array of objects with information about time spent records for the task |
| **total**   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Total number of records found |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/data-types.html) | Information about the execution time of the request |

HTTP status: **400**

```json
{
    "error":"ERROR_CORE",
    "error_description":"ACTION_NOT_ALLOWED"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** |
| --- | --- |
| `0x100002` | Access denied |
| `0x000004` | Action not allowed |
| `0x000040` | Unknown error |
| `0x000100` | Invalid method parameters provided |

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

- [Time Tracking in Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/index.html)
- [Add Time Entry task.elapseditem.add](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-add.html)
- [Update Time Entry task.elapseditem.update](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-update.html)
- [Get elapsed time record by identifier task.elapseditem.get](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get.html)
- [Delete Time Entry task.elapseditem.delete](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-delete.html)
- [Check Action Permission for task.elapseditem.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-is-action-allowed.html)
- [Get a list of methods and their descriptions task.elapseditem.getmanifest](https://apidocs.bitrix24.com/api-reference/tasks/elapsed-item/api-reference/tasks/elapsed-item/task-elapsed-item-get-manifest.html)