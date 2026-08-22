---
title: "Translate the task to \"deferred\" status task.item.defer | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-defer.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Translate the task to "deferred" status task.item.defer

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

This method changes the task status to "deferred." To perform this operation, the task must be in the [In Progress](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/task-item-start-execution.html) status.

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **TASKID** | Task identifier |

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
-d '{"TASKID":13}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.defer
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":13,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.defer
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.defer',
        [13]
    );
    
    const result = response.getData().result;
    console.info(result);
    console.log(result);
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
            'task.item.defer',
            [13]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your required data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deferring task item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.defer',
    [13],
    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.item.defer',
    [
        'TASKID' => 13
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```