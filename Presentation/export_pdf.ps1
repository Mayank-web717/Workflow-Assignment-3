$pptApp = New-Object -ComObject PowerPoint.Application
$pptPath = "d:\BPMN\October\Presentation\BPMN_Project_Presentation.pptx"
$pdfPath = "d:\BPMN\October\Presentation\BPMN_Project_Presentation.pdf"

$pres = $pptApp.Presentations.Open($pptPath, 0, 0, 0)
# 32 is ppSaveAsPDF
$pres.SaveAs($pdfPath, 32)
$pres.Close()
$pptApp.Quit()

[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pres) | Out-Null
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($pptApp) | Out-Null
[System.GC]::Collect()
[System.GC]::WaitForPendingFinalizers()

Write-Output "PDF Exported Successfully: $pdfPath"
