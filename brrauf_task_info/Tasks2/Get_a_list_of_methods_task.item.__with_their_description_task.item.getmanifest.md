---
title: "Get a list of methods task.item.* with their description task.item.getmanifest | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-get-manifest.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Get a list of methods task.item.\* with their description task.item.getmanifest

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method returns a list of methods in the form of `task.item.*` along with their descriptions.

The return value of this method is not intended for automated processing, as its format may change without notice.

The method can be useful as reference information, as it always contains up-to-date information.

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
-d '{}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.getmanifest
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.getmanifest
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.getmanifest',
        []
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
            'task.item.getmanifest',
            []
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your required data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting task manifest: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.getmanifest',
    [],
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
    'task.item.getmanifest',
    []
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```