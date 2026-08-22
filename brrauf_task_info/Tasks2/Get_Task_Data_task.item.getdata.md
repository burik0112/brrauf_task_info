---
title: "Get Task Data task.item.getdata | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-get-data.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Get Task Data task.item.getdata

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns an array of task data (`TITLE`, `DESCRIPTION`, and so on). The following [fields](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/index.html) are available.

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
-d '{"TASKID":2}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.getdata
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":2,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.getdata
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.getdata',
        [2]
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
            'task.item.getdata',
            [2]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result->data(), true);
    echo 'Full Result: ' . print_r($result, true);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting task data: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.getdata',
    [2],
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
    'task.item.getdata',
    [
        'TASKID' => 2
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```