---
title: "Get a list of custom fields task.item.userfield.getlist | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/user-field/task-item-user-field-get-list.html"
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

The method `task.item.userfield.getlist` returns a list of properties.

## Parameters

| **Parameter** / **Type** | **Description** |
| --- | --- |
| **auth**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Authorization token. |
| **ORDER**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Array for sorting the result. An array in the form `array('sort field'=>'sort direction' [, ...])`. |
| **FILTER**   [`unknown`](https://apidocs.bitrix24.com/api-reference/tasks/user-field/api-reference/data-types.html) | Array for filtering the result in the form `array('filtered field'=>'filter value' [, ...])`. Required parameter. |

## Examples

JS

PHP

BX24.js

cURL

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

try {
  const response = await $b24.callListMethod(
    'task.item.userfield.getlist',
    {
      order: { "ID": "ASC" },
      filter: { "EDIT_IN_LIST": "Y" }
    },
    (progress) => { console.log('Progress:', progress) }
  )
  const items = response.getData() || []
  for (const entity of items) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}

// fetchListMethod is preferable when working with large datasets. The method implements iterative selection using a generator, allowing data to be processed in chunks and efficiently using memory.

try {
  const generator = $b24.fetchListMethod('task.item.userfield.getlist', { order: { "ID": "ASC" }, filter: { "EDIT_IN_LIST": "Y" } }, 'ID')
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity) }
  }
} catch (error) {
  console.error('Request failed', error)
}

// callMethod provides manual control over the process of paginated data retrieval through the start parameter. Suitable for scenarios where precise control over request batches is required. However, it may be less efficient compared to fetchListMethod when dealing with large volumes of data.

try {
  const response = await $b24.callMethod('task.item.userfield.getlist', { order: { "ID": "ASC" }, filter: { "EDIT_IN_LIST": "Y" } }, 0)
  const result = response.getData().result || []
  for (const entity of result) { console.log('Entity:', entity) }
} catch (error) {
  console.error('Request failed', error)
}
```

```php
try {
    $response = $b24Service
        ->core
        ->call(
            'task.item.userfield.getlist',
            [
                'order' => [
                    'ID' => 'ASC'
                ],
                'filter' => [
                    'EDIT_IN_LIST' => 'Y'
                ]
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    // Your logic for processing data

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error getting user fields list: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    "task.item.userfield.getlist",
    {
        order:
        {
            "ID": "ASC"
        },
        filter:
        {
            "EDIT_IN_LIST": "Y"
        }
    },
    function(result)
    {
    }
);
```

```js
$appParams = array(
'auth' => 'q21g8vhcqmxdrbhqlbd2wh6ev1debppa',
'ORDER' => array('ID' => 'asc'),
'FILTER' => array('USER_TYPE_ID' => 'string')
);
```

```js
$request = 'http://your-domain.com/rest/task.item.userfield.getlist.xml?' . http_build_query($appParams);
```

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)