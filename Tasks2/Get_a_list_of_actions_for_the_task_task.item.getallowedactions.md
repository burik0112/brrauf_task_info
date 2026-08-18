---
title: "Get a list of actions for the task task.item.getallowedactions | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-get-allowed-actions.html"
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

The method returns an array of identifiers for the allowed actions on the task.

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **TASKID** | Task identifier |

## Table of identifiers and allowed actions for the task

| **Identifier** | **Description** |
| --- | --- |
| `1` | ACTION\_ACCEPT |
| `2` | ACTION\_DECLINE |
| `3` | ACTION\_COMPLETE |
| `4` | ACTION\_APPROVE |
| `5` | ACTION\_DISAPPROVE |
| `6` | ACTION\_START |
| `7` | ACTION\_DELEGATE |
| `8` | ACTION\_REMOVE |
| `9` | ACTION\_EDIT |
| `10` | ACTION\_DEFER |
| `11` | ACTION\_RENEW |
| `12` | ACTION\_CREATE |
| `13` | ACTION\_CHANGE\_DEADLINE |
| `14` | ACTION\_CHECKLIST\_ADD\_ITEMS |
| `15` | ACTION\_ELAPSED\_TIME\_ADD |
| `16` | ACTION\_CHANGE\_DIRECTOR |
| `17` | ACTION\_PAUSE |
| `18` | ACTION\_START\_TIME\_TRACKING |

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
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.getallowedactions
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":13,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.getallowedactions
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.getallowedactions',
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
            'task.item.getallowedactions',
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
    echo 'Error getting allowed actions: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.getallowedactions',
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
    'task.item.getallowedactions',
    [
        'TASKID' => 13
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```