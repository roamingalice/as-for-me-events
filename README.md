# as-for-me events

ASify 各檔活動 / 銷售 landing page 的集中管理 repo。

部署在 GitHub Pages，自訂網域 `event.as-for-me.com`。

## URL 結構

新增活動只要在 repo 開新資料夾，就會多一個對應 URL，**不用再動 GoDaddy DNS**。

| 路徑 | 用途 | URL |
|------|------|-----|
| `studio/` | ASify 教室合作 B2B 銷售頁 | https://event.as-for-me.com/studio/ |

## 新增活動頁

```bash
mkdir new-event/
# 把 index.html + 圖片資源放進去
git add new-event/ && git commit -m "add: new-event 活動頁" && git push
```

幾分鐘後 `event.as-for-me.com/new-event/` 就會上線。

## DNS

`event.as-for-me.com` 在 GoDaddy 設定：

```
Type:  CNAME
Name:  event
Value: roamingalice.github.io.
```

只設過一次，之後新活動不用再動。
