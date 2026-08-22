---
title: "Get Custom Task Field by ID task.item.userfield.get | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-get.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Get Custom Task Field by ID task.item.userfield.get

We are still updating this page

Some data may be missing here — we will fill it in shortly

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `task.item.userfield.get` returns a property by ID.

## Parameters

| **Parameter** / **Type** | **Description** |
| --- | --- |
| **auth**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Authorization token. |
| **ID**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Identifier of the custom field. |

## Examples

JS

PHP

BX24.js

cURL

```js
try
{
    const response = await $b24.callMethod(
        'task.item.userfield.get',
        {
            'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
            'ID': 77
        }
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
            'task.item.userfield.get',
            [
                'auth' => 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
                'ID'   => 77
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your required data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting user field: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.userfield.get',
    {
        'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
        'ID': 77
    },

    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

```js
$appParams = array(
    'auth' => 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
    'ID' => 77
);
```

```js
$request = 'http://your-domain.com/rest/task.item.userfield.get.xml?' . http_build_query($appParams);
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)