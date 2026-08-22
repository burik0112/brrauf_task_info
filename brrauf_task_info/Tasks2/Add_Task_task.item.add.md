---
title: "Add Task task.item.add | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-add.html"
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

This method creates a new task. It returns the identifier of the added task. The following [fields](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/index.html) are available.

## Method Parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **TASKDATA**   [`array`](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/data-types.html) | Array of data fields for the task (`TITLE`, `DESCRIPTION`, etc.) |

## Code Examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

Creating a task.

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
-d '{"fields":{"TITLE":"created via REST API at **current_datetime_here**","RESPONSIBLE_ID":1,"DEADLINE":"2013-05-13T16:06:06+02:00"}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.add
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"fields":{"TITLE":"created via REST API at **current_datetime_here**","RESPONSIBLE_ID":1,"DEADLINE":"2013-05-13T16:06:06+02:00"},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.add
```

```js
try
{
    const dt = new Date();
    const response = await $b24.callMethod(
        'task.item.add',
        [{TITLE: 'created via REST API at ' + dt.toLocaleString(), RESPONSIBLE_ID: 1, DEADLINE: '2013-05-13T16:06:06+02:00'}]
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
    $dt = new DateTime();
    $response = $b24Service
        ->core
        ->call(
            'task.item.add',
            [
                [
                    'TITLE'         => 'created via REST API at ' . $dt->format('Y-m-d H:i:s'),
                    'RESPONSIBLE_ID' => 1,
                    'DEADLINE'      => '2013-05-13T16:06:06+02:00',
                ],
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
    echo 'Error adding task item: ' . $e->getMessage();
}
```

```js
var dt = new Date();
BX24.callMethod(
    'task.item.add',
    [{TITLE: 'created via REST API at ' + dt.toLocaleString(), RESPONSIBLE_ID: 1, DEADLINE: '2013-05-13T16:06:06+02:00'}],
    function(result)
    {
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$dt = new DateTime();
$title = 'created via REST API at ' . $dt->format('Y-m-d H:i:s');

$result = CRest::call(
    'task.item.add',
    [
        'fields' => [
            'TITLE' => $title,
            'RESPONSIBLE_ID' => 1,
            'DEADLINE' => '2013-05-13T16:06:06+02:00'
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

Example of recording values with CRM.

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
-d '{"TASKID":1,"FIELDS":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"]}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"TASKID":1,"FIELDS":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"]},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.update
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.update',
        [1, {UF_CRM_TASK: ["L_4", "C_7", "CO_5", "D_10"]}]
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
            'task.item.update',
            [
                1,
                ['UF_CRM_TASK' => ["L_4", "C_7", "CO_5", "D_10"]],
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
    echo 'Error updating task item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.update',
    [1, {UF_CRM_TASK: ["L_4", "C_7", "CO_5", "D_10"]}],
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
    'task.item.update',
    [
        'TASKID' => 1,
        'FIELDS' => [
            'UF_CRM_TASK' => ["L_4", "C_7", "CO_5", "D_10"]
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

The numbers are the `ID` of the corresponding values. The value `L_4` indicates a link to the lead task with `ID = 4`. Multiple links of the same type can be specified, for example, `L_4, L_5`.

- `L` — lead
- `C` — contact
- `CO` — company
- `D` — deal