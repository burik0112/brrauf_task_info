---
title: "Get the list of fields tasks.task.getFields | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-get-fields.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.task.getFields` returns the description of standard and custom fields of a task.

## Method Parameters

No parameters.

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
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.getFields
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.getFields
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.getFields',
        {}
    );
    
    const result = response.getData().result;
    console.log('Task fields:', result);
    
    processResult(result);
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
            'tasks.task.getFields',
            []
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error fetching task fields: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.getFields',
    {},
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.getFields',
    []
);

echo '<PRE>';
print_r($result);
echo '</PRE>';
```

## Response Handling

HTTP status: **200**

```json
{
    "result": {
        "fields": {
            "ID": {
                "title": "ID",
                "type": "integer",
                "primary": true
            },
            "PARENT_ID": {
                "title": "Base task ID",
                "type": "integer",
                "default": 0
            },
            "TITLE": {
                "title": "Title",
                "type": "string",
                "required": true
            },
            "DESCRIPTION": {
                "title": "Description",
                "type": "string"
            },
            "MARK": {
                "title": "Rating",
                "type": "enum",
                "values": {
                    "N": "Negative",
                    "P": "Positive"
                },
                "default": null
            },
            "PRIORITY": {
                "title": "Priority",
                "type": "enum",
                "values": {
                    "2": "High",
                    "1": "Medium",
                    "0": "Low"
                },
                "default": 1
            },
            "STATUS": {
                "title": "Status",
                "type": "enum",
                "values": {
                    "2": "Pending",
                    "3": "In Progress",
                    "4": "Awaiting Control",
                    "5": "Completed",
                    "6": "Deferred"
                },
                "default": 2
            },
            "MULTITASK": {
                "title": "Multitask",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "NOT_VIEWED": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "REPLICATE": {
                "title": "Recurring task",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "GROUP_ID": {
                "title": "Project",
                "type": "integer",
                "default": 0
            },
            "STAGE_ID": {
                "title": "Stage",
                "type": "integer",
                "default": 0
            },
            "SPRINT_ID": {
                "title": "Sprint",
                "type": "integer",
                "default": 0
            },
            "BACKLOG_ID": {
                "title": "Backlog",
                "type": "integer",
                "default": 0
            },
            "CREATED_BY": {
                "title": "Creator",
                "type": "integer",
                "required": true
            },
            "CREATED_DATE": {
                "title": null,
                "type": "datetime"
            },
            "RESPONSIBLE_ID": {
                "title": "Assignee",
                "type": "integer",
                "required": true
            },
            "ACCOMPLICES": {
                "title": null,
                "type": "array"
            },
            "AUDITORS": {
                "title": null,
                "type": "array"
            },
            "CHANGED_BY": {
                "title": "Changed by",
                "type": "integer"
            },
            "CHANGED_DATE": {
                "title": "Change date",
                "type": "datetime"
            },
            "STATUS_CHANGED_BY": {
                "title": "Status changed by",
                "type": "integer"
            },
            "STATUS_CHANGED_DATE": {
                "title": "Status change date",
                "type": "datetime"
            },
            "CLOSED_BY": {
                "title": "Closed by",
                "type": "integer",
                "default": null
            },
            "CLOSED_DATE": {
                "title": "Closing date",
                "type": "datetime",
                "default": null
            },
            "ACTIVITY_DATE": {
                "title": null,
                "type": "datetime",
                "default": null
            },
            "DATE_START": {
                "title": "Start date",
                "type": "datetime",
                "default": null
            },
            "DEADLINE": {
                "title": "Deadline",
                "type": "datetime",
                "default": null
            },
            "START_DATE_PLAN": {
                "title": "Planned start",
                "type": "datetime",
                "default": null
            },
            "END_DATE_PLAN": {
                "title": "Planned completion",
                "type": "datetime",
                "default": null
            },
            "GUID": {
                "title": "GUID",
                "type": "string",
                "default": null
            },
            "XML_ID": {
                "title": "XML_ID",
                "type": "string",
                "default": null
            },
            "COMMENTS_COUNT": {
                "title": "Number of comments",
                "type": "integer",
                "default": 0
            },
            "SERVICE_COMMENTS_COUNT": {
                "title": null,
                "type": "integer",
                "default": 0
            },
            "NEW_COMMENTS_COUNT": {
                "title": null,
                "type": "integer",
                "default": 0
            },
            "ALLOW_CHANGE_DEADLINE": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "ALLOW_TIME_TRACKING": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "TASK_CONTROL": {
                "title": "Accept work",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "ADD_IN_REPORT": {
                "title": "Add to report",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "FORKED_BY_TEMPLATE_ID": {
                "title": "Created from template",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "TIME_ESTIMATE": {
                "title": "Estimated time",
                "type": "integer"
            },
            "TIME_SPENT_IN_LOGS": {
                "title": "Time spent from change history",
                "type": "integer"
            },
            "MATCH_WORK_TIME": {
                "title": "Skip weekends",
                "type": "integer"
            },
            "FORUM_TOPIC_ID": {
                "title": "FORUM_TOPIC_ID",
                "type": "integer"
            },
            "FORUM_ID": {
                "title": "FORUM_ID",
                "type": "integer"
            },
            "SITE_ID": {
                "title": "SITE_ID",
                "type": "string"
            },
            "SUBORDINATE": {
                "title": "Subordinate task",
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": null
            },
            "FAVORITE": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": null
            },
            "EXCHANGE_MODIFIED": {
                "title": "EXCHANGE_MODIFIED",
                "type": "datetime",
                "default": null
            },
            "EXCHANGE_ID": {
                "title": "EXCHANGE_ID",
                "type": "integer",
                "default": null
            },
            "OUTLOOK_VERSION": {
                "title": "OUTLOOK_VERSION",
                "type": "integer",
                "default": null
            },
            "VIEWED_DATE": {
                "title": "Last viewed date",
                "type": "datetime"
            },
            "SORTING": {
                "title": "Sorting index",
                "type": "double"
            },
            "DURATION_PLAN": {
                "title": "Spent (planned)",
                "type": "integer"
            },
            "DURATION_FACT": {
                "title": "Spent (actual)",
                "type": "integer"
            },
            "CHECKLIST": {
                "title": null,
                "type": "array"
            },
            "DURATION_TYPE": {
                "title": "DURATION_TYPE",
                "type": "enum",
                "values": [
                    "secs",
                    "mins",
                    "hours",
                    "days",
                    "weeks",
                    "monts",
                    "years"
                ],
                "default": "days"
            },
            "IS_MUTED": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "IS_PINNED": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "IS_PINNED_IN_GROUP": {
                "title": null,
                "type": "enum",
                "values": {
                    "Y": "Yes",
                    "N": "No"
                },
                "default": "N"
            },
            "FLOW_ID": {
                "title": "Flow",
                "type": "integer",
                "default": 0
            },
            "UF_CRM_TASK": {
                "title": "CRM entities",
                "type": "crm"
            },
            "UF_TASK_WEBDAV_FILES": {
                "title": "Upload files",
                "type": "disk_file"
            },
            "UF_MAIL_MESSAGE": {
                "title": null,
                "type": "mail_message"
            },
            "UF_NEW_TASKS_FIELD": {
                "title": "New task field",
                "type": "string"
            }
        }
    },
    "time": {
        "start": 1758790899,
        "finish": 1758790899.809331,
        "duration": 0.809330940246582,
        "processing": 0,
        "date_start": "2025-09-25T12:01:39+02:00",
        "date_finish": "2025-09-25T12:01:39+02:00",
        "operating_reset_at": 1758791499,
        "operating": 0
    }
}
```

### Returned Data

| **Title**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with [task field descriptions](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html) |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue Learning

- [Get Task by ID tasks.task.get](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-get.html)
- [Get the list of tasks tasks.task.list](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html)