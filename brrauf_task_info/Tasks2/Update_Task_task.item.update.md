---
title: "Update Task task.item.update | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/task-item-update.html"
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

This method updates the data for a task. The following [fields](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/index.html) are available for updating. When updating task data, business logic and permissions are taken into account. For example, the Assignee cannot rename the task — in such cases, an error will be generated.

It is recommended to check if the action is allowed before updating the data ([task.item.isactionallowed](https://apidocs.bitrix24.com/api-reference/tasks/deprecated/task-item/api-reference/tasks/deprecated/task-item/task-item-is-action-allowed.html)).

## Method Parameters

| **Name** | **Description** |
| --- | --- |
| **TASKID** | Task identifier. |
| **TASKDATA** | List of fields with new values. |

The order of parameters in the request must be followed. If it is violated, the request will be executed with errors.

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
-d '{"taskId":1,"fields":{"TIME_ESTIMATE":113}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":1,"fields":{"TIME_ESTIMATE":113},"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/task.item.update
```

```js
try
{
    const response = await $b24.callMethod(
        'task.item.update',
        [1, {TIME_ESTIMATE: 113}]
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
                ['TIME_ESTIMATE' => 113],
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    // Your data processing logic
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error updating task item: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'task.item.update',
    [1, {TIME_ESTIMATE: 113}],
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
        'taskId' => 1,
        'fields' => [
            'TIME_ESTIMATE' => 113
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
-d '{"taskId":1,"fields":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"]}}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/task.item.update
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":1,"fields":{"UF_CRM_TASK":["L_4","C_7","CO_5","D_10"]},"auth":"**put_access_token_here**"}' \
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
    // Your data processing logic
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
        'taskId' => 1,
        'fields' => [
            'UF_CRM_TASK' => ["L_4", "C_7", "CO_5", "D_10"]
        ]
    ]
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

The numbers are the `IDs` of the corresponding values. The value `L_4` indicates a link to the lead task with `ID = 4`. Multiple links of the same type can be specified, for example, `L_4, L_5`. The following designations are available:

- `L` — lead
- `C` — contact
- `CO` — company
- `D` — deal