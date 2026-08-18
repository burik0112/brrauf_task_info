---
title: "Delete file attachment from task task.item.deletefile | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-delete-file.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Delete file attachment from task task.item.deletefile

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

This method removes the file attachment from a task.

## Method parameters

| **Name** | **Description** |
| --- | --- |
| **auth** | Authorization token |
| **TASK\_ID** | Task identifier |
| **ATTACHMENT\_ID** | Identifier of the attached file |

## Code examples

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
-d '{"TASK_ID":3,"ATTACHMENT_ID":28}' \
https://your-domain.com/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.deletefile
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASK_ID":3,"ATTACHMENT_ID":28,"auth":"1iqeuq94vzfxu01bouws3voja2lsezfq"}' \
https://your-domain.com/rest/task.item.deletefile
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.deletefile',
        {
            TASK_ID: 3,
            ATTACHMENT_ID: 28
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
            'task.item.deletefile',
            [
                'TASK_ID'       => 3,
                'ATTACHMENT_ID' => 28
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
    echo 'Error deleting file: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.deletefile',
    {
        TASK_ID: 3,
        ATTACHMENT_ID: 28
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
    'task.item.deletefile',
    [
        'TASK_ID' => 3,
        'ATTACHMENT_ID' => 28
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```