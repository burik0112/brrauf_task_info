---
title: "Delegate Task task.item.delegate | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-delegate.html"
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

This method delegates a task to a new user.

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **TASKID** | Task identifier |
| **USERID** | Identifier of the new Assignee (responsible) |

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
-d '{"TASKID":13,"USERID":3}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.delegate
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":13,"USERID":3,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.delegate
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.delegate',
        [13, 3]
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
            'task.item.delegate',
            [13, 3]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your logic for processing data
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error delegating task item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.delegate',
    [13, 3],
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
    'task.item.delegate',
    [
        'TASKID' => 13,
        'USERID' => 3
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```