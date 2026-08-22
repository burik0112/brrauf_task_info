---
title: "Remove Task from Favorites task.item.deletefromfavorite | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-delete-from-favorite.html"
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

This method removes a task from Favorites.

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **auth** | Authorization token |
| **TASK\_ID** | Task identifier |
| **PARAMS** | The parameter contains the key `AFFECT_CHILDREN`. It indicates whether to add the subtasks of this task to Favorites |

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
-d '{"TASK_ID":10,"PARAMS":{"AFFECT_CHILDREN":"Y"}}' \
https://your-domain.com/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.deletefromfavorite
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASK_ID":10,"PARAMS":{"AFFECT_CHILDREN":"Y"},"auth":"mqa17fnd5cth4rpwtizyl49tbnzp7omf"}' \
https://your-domain.com/rest/task.item.deletefromfavorite
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.deletefromfavorite',
        {
            TASK_ID: 10,
            PARAMS: {
                AFFECT_CHILDREN: "Y"
            }
        }
    );
    
    const result = response.getData().result;
    console.log(result);
}
catch( error )
{
    console.error(error);
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.item.deletefromfavorite',
            [
                'TASK_ID' => 10,
                'PARAMS' => [
                    'AFFECT_CHILDREN' => "Y"
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deleting task from favorites: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.deletefromfavorite',
    {
        TASK_ID: 10,
        PARAMS: {
            AFFECT_CHILDREN: "Y"
        }
    },
    function(result) {
        if(result.error())
            console.error(result.error());
        else
            console.log(result.data());
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'task.item.deletefromfavorite',
    [
        'TASK_ID' => 10,
        'PARAMS' => [
            'AFFECT_CHILDREN' => 'Y'
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```