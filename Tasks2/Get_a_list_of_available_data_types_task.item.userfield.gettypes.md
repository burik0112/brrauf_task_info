---
title: "Get a list of available data types task.item.userfield.gettypes | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-get-types.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Get a list of available data types task.item.userfield.gettypes

We are still updating this page

Some data may be missing here — we will fill it in shortly

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `task.item.userfield.gettypes` returns all available data types in the system.

Custom fields in tasks support the following data types:

- `string` — string
- `double` — number
- `date` — date
- `boolean` — yes/no

## Parameters

| **Parameter** / **Type** | **Description** |
| --- | --- |
| **auth**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Authorization token. |

## Examples

JS

PHP

BX24.js

cURL

```js
try
{
    const response = await $b24.callMethod(
        'task.item.userfield.gettypes',
        {'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa'}
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
            'task.item.userfield.gettypes',
            [
                'auth' => 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
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
    echo 'Error getting user field types: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.userfield.gettypes',
    {'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa'},

    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

```js
$request = 'http://your-domain.com/rest/task.item.userfield.gettypes.xml?' . http_build_query($appParams);
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)