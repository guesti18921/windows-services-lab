while ($true) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

    $message = "[$timestamp] PowerShell background monitor. Status: OK"

    Add-Content -Path "C:\ps_service_log.txt" -Value $message

    Start-Sleep -Seconds 5
}