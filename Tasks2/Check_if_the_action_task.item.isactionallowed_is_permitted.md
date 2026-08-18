---
title: "Check if the action task.item.isactionallowed is permitted | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-is-action-allowed.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns `true` if the action is permitted. Otherwise, it will return `false`.

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **TASKID** | Task identifier |
| **ACTIONID** | Identifier of the action being checked (see the constants of the method [task.item.getallowedactions](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/task-item-get-allowed-actions.html)) |

It is mandatory to follow the order of parameters in the request. If this order is violated, the request will be executed with errors.

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
-d '{"TASKID":13,"ACTION":6}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.isactionallowed
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":13,"ACTION":6,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.isactionallowed
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.isactionallowed',
        [13, 6]
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
            'task.item.isactionallowed',
            [13, 6]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your logic for processing data
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error checking if action is allowed: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.isactionallowed',
    [13, 6],
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
    'task.item.isactionallowed',
    [
        'TASKID' => 13,
        'ACTION' => 6
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```