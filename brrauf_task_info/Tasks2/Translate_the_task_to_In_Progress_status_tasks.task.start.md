---
title: "Translate the task to In Progress status tasks.task.start | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/tasks/tasks-task-start.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/scopes/permissions.html)
> 
> Who can execute the method:
> 
> - any user with access to edit the task
> - Creator, Assignee, and Participants of the task

The method `tasks.task.start` changes the task status to In Progress.

## Method Parameters

Required parameters are marked with \*

| **Name**   `type` | **Description** |
| --- | --- |
| **taskId** \*   [`integer`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Task identifier.  The task identifier can be obtained when [creating a new task](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-add.html) or by using the [get task list method](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-list.html) |

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
-d '{"taskId":1}' \
https://**put_your_bitrix24_address**/rest/**put_your_user_id_here**/**put_your_webhook_here**/tasks.task.start
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{"taskId":1,"auth":"**put_access_token_here**"}' \
https://**put_your_bitrix24_address**/rest/tasks.task.start
```

```javascript
try
{
    const response = await $b24.callMethod(
        'tasks.task.start',
        {
            taskId: 1,
        }
    );
    
    const result = response.getData().result;
    console.log('Deferred task with ID:', result);
    
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
            'tasks.task.start',
            [
                'taskId' => 1
            ]
        );

    $result = $response
        ->getResponseData()
        ->getResult();

    echo 'Success: ' . print_r($result, true);
    processData($result);

} catch (Throwable $e) {
    error_log($e->getMessage());
    echo 'Error deferring task: ' . $e->getMessage();
}
```

```js
BX24.callMethod(
    'tasks.task.start',
    {
        'taskId': 1
    },
    function(result){
        console.info(result.data());
        console.log(result);
    }
);
```

```php
require_once('crest.php');

$result = CRest::call(
    'tasks.task.start',
    [
        'taskId' => 1
    ]
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
        "task": {
            "id": "8017",
            "parentId": "7817",
            "title": "Task Example",
            "description": "Task description with [B]formatting[/B]",
            "mark": "P",
            "priority": "2",
            "multitask": "N",
            "notViewed": "N",
            "replicate": "Y",
            "stageId": "351",
            "sprintId": null,
            "backlogId": "5",
            "createdBy": "503",
            "createdDate": "2025-06-04T16:15:55+02:00",
            "responsibleId": "503",
            "changedBy": "503",
            "changedDate": "2025-09-09T16:32:43+02:00",
            "statusChangedBy": "503",
            "closedBy": "0",
            "closedDate": null,
            "activityDate": "2025-09-09T16:31:11+02:00",
            "dateStart": "2025-09-09T16:32:43+02:00",
            "deadline": "2025-09-19T17:00:00+02:00",
            "startDatePlan": null,
            "endDatePlan": null,
            "guid": "{21e7b78d-498e-4c84-a896-2dbeb26861b8}",
            "xmlId": null,
            "commentsCount": "40",
            "serviceCommentsCount": "24",
            "allowChangeDeadline": "Y",
            "allowTimeTracking": "Y",
            "taskControl": "Y",
            "addInReport": "N",
            "forkedByTemplateId": null,
            "timeEstimate": "101580",
            "timeSpentInLogs": "69963",
            "matchWorkTime": "N",
            "forumTopicId": "1273",
            "forumId": "11",
            "siteId": "s1",
            "subordinate": "Y",
            "exchangeModified": null,
            "exchangeId": null,
            "outlookVersion": "43",
            "viewedDate": "2025-09-09T16:31:11+02:00",
            "sorting": null,
            "durationFact": "1166",
            "isMuted": "Y",
            "isPinned": "N",
            "isPinnedInGroup": "N",
            "flowId": null,
            "descriptionInBbcode": "Y",
            "status": "3",
            "statusChangedDate": "2025-09-09T16:32:43+02:00",
            "durationPlan": "0",
            "durationType": "days",
            "favorite": "Y",
            "groupId": "125",
            "auditors": [
                "61",
                "103",
                "547"
            ],
            "accomplices": [
                "3",
                "11"
            ],
            "checklist": {
                "433": {
                    "id": "433",
                    "taskId": "8017",
                    "createdBy": "503",
                    "parentId": "431",
                    "title": "First",
                    "sortIndex": "0",
                    "isComplete": "N",
                    "isImportant": "N",
                    "toggledBy": null,
                    "toggledDate": null,
                    "ufChecklistFiles": false,
                    "members": [],
                    "attachments": [],
                    "entityId": "8017",
                    "action": {
                        "modify": true,
                        "remove": true,
                        "toggle": true,
                        "add": true,
                        "addAccomplice": true
                    }
                },
                "431": {
                    "id": "431",
                    "taskId": "8017",
                    "createdBy": "503",
                    "parentId": 0,
                    "title": "Checklist 1",
                    "sortIndex": "0",
                    "isComplete": "N",
                    "isImportant": "N",
                    "toggledBy": null,
                    "toggledDate": null,
                    "ufChecklistFiles": false,
                    "members": [],
                    "attachments": [],
                    "entityId": "8017",
                    "action": {
                        "modify": true,
                        "remove": true,
                        "toggle": true,
                        "add": true,
                        "addAccomplice": true
                    }
                },
                "435": {
                    "id": "435",
                    "taskId": "8017",
                    "createdBy": "503",
                    "parentId": "431",
                    "title": "Second",
                    "sortIndex": "1",
                    "isComplete": "N",
                    "isImportant": "N",
                    "toggledBy": null,
                    "toggledDate": null,
                    "ufChecklistFiles": false,
                    "members": [],
                    "attachments": [],
                    "entityId": "8017",
                    "action": {
                        "modify": true,
                        "remove": true,
                        "toggle": true,
                        "add": true,
                        "addAccomplice": true
                    }
                }
            },
            "group": {
                "id": "125",
                "name": "Workgroup",
                "opened": false,
                "membersCount": 1,
                "image": "\/bitrix\/images\/socialnetwork\/workgroup\/bag.png",
                "additionalData": []
            },
            "creator": {
                "id": "503",
                "name": "Maria Ivanova",
                "link": "\/company\/personal\/user\/503\/",
                "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/45749\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/c89\/c89c6b7301880958ea704b5a8470635c\/4R5A1256.png",
                "workPosition": "Administrator"
            },
            "responsible": {
                "id": "503",
                "name": "Maria Ivanova",
                "link": "\/company\/personal\/user\/503\/",
                "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/45749\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/c89\/c89c6b7301880958ea704b5a8470635c\/4R5A1256.png",
                "workPosition": "Administrator"
            },
            "accomplicesData": {
                "3": {
                    "id": "3",
                    "name": "Andrew Karpov",
                    "link": "\/company\/personal\/user\/3\/",
                    "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/249\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/cd526b0644e7ff4d794ea41cb36bc423\/odmin.png",
                    "workPosition": "System Administrator"
                },
                "11": {
                    "id": "11",
                    "name": "Andrew Sergeev",
                    "link": "\/company\/personal\/user\/11\/",
                    "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/231\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/026bf59e161a0bd50f401d3796800651\/66b.jpg",
                    "workPosition": "Specialist"
                }
            },
            "auditorsData": {
                "61": {
                    "id": "61",
                    "name": "Ivan Petrov",
                    "link": "\/company\/personal\/user\/61\/",
                    "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/8674\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/7b5\/7b52e4c2304ec0520dab3d4261e9ca1f\/sp.jpg",
                    "workPosition": "Marketer"
                },
                "103": {
                    "id": "103",
                    "name": "Svetlana Ivanova",
                    "link": "\/company\/personal\/user\/103\/",
                    "icon": "https:\/\/mysite.com\/b17053\/resize_cache\/8644\/c0120a8d7c10d63c83e32398d1ec4d9e\/main\/45f\/45fff10d17d398a5583184c8350cd197\/buh.jpg",
                    "workPosition": "Accountant"
                },
                "547": {
                    "id": "547",
                    "name": "Maria",
                    "link": "\/company\/personal\/user\/547\/",
                    "icon": "\/bitrix\/images\/tasks\/default_avatar.png",
                    "workPosition": "Tester"
                }
            },
            "newCommentsCount": 0,
            "action": {
                "accept": false,
                "decline": false,
                "complete": true,
                "approve": false,
                "disapprove": false,
                "start": false,
                "pause": true,
                "delegate": true,
                "remove": true,
                "edit": true,
                "defer": false,
                "renew": false,
                "create": true,
                "changeDeadline": true,
                "checklistAddItems": true,
                "addFavorite": false,
                "deleteFavorite": true,
                "rate": true,
                "take": false,
                "edit.originator": false,
                "checklist.reorder": true,
                "elapsedtime.add": true,
                "dayplan.timer.toggle": true,
                "edit.plan": true,
                "checklist.add": true,
                "favorite.add": false,
                "favorite.delete": true
            },
            "checkListTree": {
                "nodeId": 0,
                "fields": {
                    "id": null,
                    "copiedId": null,
                    "entityId": null,
                    "userId": 503,
                    "createdBy": null,
                    "parentId": null,
                    "title": "",
                    "sortIndex": null,
                    "displaySortIndex": "",
                    "isComplete": false,
                    "isImportant": false,
                    "completedCount": 0,
                    "members": [],
                    "attachments": [],
                    "nodeId": null
                },
                "action": [],
                "descendants": [
                    {
                        "nodeId": 1,
                        "fields": {
                            "id": 431,
                            "copiedId": null,
                            "entityId": 8017,
                            "userId": 503,
                            "createdBy": 503,
                            "parentId": 0,
                            "title": "Checklist 1",
                            "sortIndex": 0,
                            "displaySortIndex": "",
                            "isComplete": false,
                            "isImportant": false,
                            "completedCount": 0,
                            "members": [],
                            "attachments": [],
                            "nodeId": null
                        },
                        "action": {
                            "modify": true,
                            "remove": true,
                            "toggle": true,
                            "add": true,
                            "addAccomplice": true
                        },
                        "descendants": [
                            {
                                "nodeId": 2,
                                "fields": {
                                    "id": 433,
                                    "copiedId": null,
                                    "entityId": 8017,
                                    "userId": 503,
                                    "createdBy": 503,
                                    "parentId": 431,
                                    "title": "First",
                                    "sortIndex": 0,
                                    "displaySortIndex": "1",
                                    "isComplete": false,
                                    "isImportant": false,
                                    "completedCount": 0,
                                    "members": [],
                                    "attachments": [],
                                    "nodeId": null
                                },
                                "action": {
                                    "modify": true,
                                    "remove": true,
                                    "toggle": true,
                                    "add": true,
                                    "addAccomplice": true
                                },
                                "descendants": []
                            },
                            {
                                "nodeId": 3,
                                "fields": {
                                    "id": 435,
                                    "copiedId": null,
                                    "entityId": 8017,
                                    "userId": 503,
                                    "createdBy": 503,
                                    "parentId": 431,
                                    "title": "Second",
                                    "sortIndex": 1,
                                    "displaySortIndex": "2",
                                    "isComplete": false,
                                    "isImportant": false,
                                    "completedCount": 0,
                                    "members": [],
                                    "attachments": [],
                                    "nodeId": null
                                },
                                "action": {
                                    "modify": true,
                                    "remove": true,
                                    "toggle": true,
                                    "add": true,
                                    "addAccomplice": true
                                },
                                "descendants": []
                            }
                        ]
                    }
                ]
            },
            "checkListCanAdd": true
        },
        "time": {
            "start": 1757424763.612856,
            "finish": 1757424763.90201,
            "duration": 0.289154052734375,
            "processing": 0.26647090911865234,
            "date_start": "2025-09-09T16:32:43+02:00",
            "date_finish": "2025-09-09T16:32:43+02:00",
            "operating_reset_at": 1757425363,
            "operating": 0.26645517349243164
        }
    }
}
```

### Returned Data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with response data |
| **task**   [`object`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html) | Object with [task description](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/fields.html) after the operation is performed |
| **time**   [`time`](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/data-types.html#time) | Information about the request execution time |

HTTP status: **400**

```json
{
    "error":"0",
    "error_description":"Action on the task is not allowed"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Description** | **Value** |
| --- | --- | --- |
| `0` | wrong task id | The value of `taskId` is of an incorrect type |
| `0` | Action on the task is not allowed | This error is returned in cases:  - the task with the specified `ID` does not exist - no access to the task - no rights to perform the action on the task |

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

- [Tasks: Overview of Methods](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/index.html)
- [Translate task to Waiting for execution status tasks.task.pause](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-pause.html)
- [Translate the task to Deferred status tasks.task.defer](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-defer.html)
- [Translate task to Completed status tasks.task.complete](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-complete.html)
- [Renew a task after its completion tasks.task.renew](https://apidocs.bitrix24.com/api-reference/tasks/api-reference/tasks/tasks-task-renew.html)