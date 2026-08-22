---
title: "Update User Field task.item.userfield.update | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-update.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
## Update User Field task.item.userfield.update

We are still updating this page

Some data may be missing here — we will complete it shortly

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/scopes/permissions.html)
> 
> Who can execute the method: administrator

The method `task.item.userfield.update` is used to edit the properties' parameters.

## Parameters

| **Parameter** / **Type** | **Description** |
| --- | --- |
| **auth**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Authorization token. |
| **ID**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Identifier of the user field. |
| **DATA**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Array `array('field'=>'value', ...)`. Contains values of the parameters to be edited. |

## Examples

JS

PHP

BX24.js

cURL

```js
try
{
    const response = await $b24.callMethod(
        'task.item.userfield.update',
        {
            'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
            'ID': 77,
            'DATA': {'XML_ID': 'new_external_id'}
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
            'task.item.userfield.update',
            [
                'auth' => 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
                'ID' => 77,
                'DATA' => ['XML_ID' => 'new_external_id']
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
    echo 'Error updating user field: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.userfield.update',
    {
        'auth': 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
        'ID': 77,
        'DATA': {'XML_ID': 'new_external_id'}
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
    'ID' => 77,
    'DATA' => array('XML_ID' => 'new_external_id')
);
```

```js
$request = 'http://your-domain.com/rest/task.item.userfield.update.xml?' . http_build_query($appParams);
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)