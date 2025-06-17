generer_tous_les_chiffres() {
    chiffres := []
    Loop, 100000000 {
        chiffre := SubStr("00000000" . A_Index, -8)  ; Formatage avec 8 chiffres
        chiffres.Push(chiffre)
    }
    return chiffres
}

chiffres := generer_tous_les_chiffres()

; Ouvrir Internet Explorer et naviguer vers une page Web (remplacez l'URL par la vôtre)
IE := ComObjCreate("InternetExplorer.Application")
IE.Visible := true
IE.Navigate("https://svt-erlich.fr/seconde/enseignement-obligatoire/theme-2-la-terre-la-vie-et-lorganisation-du-vivant/")  ; Remplacez par l'URL souhaitée

; Attendre que la page se charge (ajustez le temps d'attente si nécessaire)
While IE.ReadyState != 4 || IE.Busy
    Sleep, 1000

; Obtenez les coordonnées X et Y de l'élément spécifique
X := 218.75
Y := 218.75

; Cliquez à l'emplacement spécifique sur la page
MouseClick, left, %X%, %Y%

; Attendre un court instant (ajustez si nécessaire)
Sleep, 1000

; Boucle pour envoyer chaque chiffre à un emplacement spécifique sur la page
Loop, % chiffres.MaxIndex() {
    chiffre := chiffres[A_Index]
    
    ; Copier le chiffre dans le presse-papiers
    Clipboard := chiffre
    
    ; Coller le chiffre dans l'élément de la page Web (ajustez l'élément selon votre page)
    ; Cette étape dépend de la structure de la page web, vous pouvez utiliser des commandes
    ; comme Document.GetElementById ou Document.GetElementsByName pour cibler l'élément souhaité.
    ; Voici un exemple générique :
    IE.Document.GetElementById("champ").value := chiffre
    
    ; Appuyer sur Entrée
    Send, {Enter}
    
    ; Attendre un certain temps (ajustez si nécessaire)
    Sleep, 1000
}

; Fermer Internet Explorer
IE.Quit()
IE := ""
