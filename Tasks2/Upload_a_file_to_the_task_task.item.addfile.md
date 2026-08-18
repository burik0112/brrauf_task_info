---
title: "Upload a file to the task task.item.addfile | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-add-file.html"
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

This method uploads a file to a task. Currently, file upload is implemented via `post` with the file content passed in the `CONTENT` parameter.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **TASK\_ID** | Task identifier |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/data-types.html) | File name |
| **CONTENT** | File content in `base64` format |

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
-d '{"TASK_ID":"140","FILE":{"NAME":"desc.txt","CONTENT":"BASE64_ENCODED_CONTENT_OF_DESC.TXT"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.addfile
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASK_ID":"140","FILE":{"NAME":"desc.txt","CONTENT":"BASE64_ENCODED_CONTENT_OF_DESC.TXT"},"auth":"z3eamwwkpgl7u18kx14q1s4c0ffckqsn"}' \
https://**put_your_bitrix24_address**/rest/task.item.addfile
```

```js
try
{
    const response = await $b24.callMethod(
        "task.item.addfile",
        {
            TASK_ID: "140",
            FILE: {
                NAME: "desc.txt",
                CONTENT: "BASE64_ENCODED_CONTENT_OF_DESC.TXT"
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
            'task.item.addfile',
            [
                'TASK_ID' => '140',
                'FILE'    => [
                    'NAME'    => 'desc.txt',
                    'CONTENT' => 'BASE64_ENCODED_CONTENT_OF_DESC.TXT',
                ],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    if ($result->error()) {
        error_log($result->error());
        echo 'Error: ' . $result->error();
    } else {
        echo 'Success: ' . print_r($result->data(), true);
    }

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error adding file to task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    "task.item.addfile",
    {
        TASK_ID: "140",
        FILE: {
            NAME: "desc.txt",
            CONTENT: "BASE64_ENCODED_CONTENT_OF_DESC.TXT"
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
    'task.item.addfile',
    [
        'TASK_ID' => "140",
        'FILE' => [
            'NAME' => 'desc.txt',
            'CONTENT' => base64_encode(file_get_contents($_SERVER['DOCUMENT_ROOT'] .'/desc.txt'))
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```