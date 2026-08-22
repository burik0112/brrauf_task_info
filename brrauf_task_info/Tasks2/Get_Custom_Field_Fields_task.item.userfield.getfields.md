---
title: "Get Custom Field Fields task.item.userfield.getfields | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-get-fields.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
We are still updating this page

Some data may be missing here — we will fill it in shortly

> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `task.item.userfield.getfields` returns all available fields.

## Parameters

No parameters.

## Example

JS

PHP

BX24.js

```js
try
{
    const response = await $b24.callMethod(
        'task.item.userfield.getfields',
        {}
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
            'task.item.userfield.getfields',
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
    echo 'Error getting user fields: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.userfield.getfields',
    {},
    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

## List of Fields

| **Code** / **Type** | **Field** | **Note** |
| --- | --- | --- |
| **ID**   [`int`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Identifier | Read-only |
| **ENTITY\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Object |  |
| **FIELD\_NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Code | Immutable |
| **USER\_TYPE\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Data type | Immutable |
| **XML\_ID**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | External identifier (XML ID) |  |
| **SORT**   [`int`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Sorting |  |
| **MULTIPLE**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Multiple |  |
| **MANDATORY**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Mandatory |  |
| **SHOW\_FILTER**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Show in list filter |  |
| **SHOW\_IN\_LIST**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Show in list |  |
| **EDIT\_IN\_LIST**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Allow user editing |  |
| **IS\_SEARCHABLE**   [`char`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Field values participate in search |  |
| **EDIT\_FORM\_LABEL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Label in edit form |  |
| **LIST\_COLUMN\_LABEL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Header in list |  |
| **LIST\_FILTER\_LABEL**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Filter label in list |  |
| **ERROR\_MESSAGE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Error message |  |
| **HELP\_MESSAGE**   [`string`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Help |  |
| **LIST**   [`uf_enum_element`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | List elements | Multiple |
| **SETTINGS**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Additional settings (depend on type) |  |