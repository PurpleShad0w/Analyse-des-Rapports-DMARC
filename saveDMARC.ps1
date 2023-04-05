$outlook = new-object -com outlook.application
$mapi = $outlook.GetNameSpace("MAPI")
$olDefaultFolderInbox = 6
$inbox = $mapi.GetDefaultFolder($olDefaultFolderInbox)
$inbox.Folders | SELECT FolderPath