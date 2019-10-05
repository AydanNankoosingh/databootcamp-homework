Attribute VB_Name = "Module1"
Sub SummarizeData():
    
    Dim stock As String
    Dim open1 As Double
    Dim close1 As Double
    Dim totvol As Double
    Dim change As Double
    
    Dim i, j, k, l As Integer
        
    ' variables for challange table
    Dim biginc, bigdec, bigvol As Double
    
            
    j = 1
    
    ' loop through each worksheet
    Do While j <= Worksheets.Count

        ' select ticker name of first stock on first worksheet
        Worksheets(j).Select
        
        ' summary table headers
        Cells(1, 10).Value = "Ticker Symbol"
        Cells(1, 11).Value = "Yearly Change"
        Cells(1, 12).Value = "Percent Change"
        Cells(1, 13).Value = "Total Volume"
    
        ' autofit the table column widths
        Range("J1", "N1").Columns.AutoFit


        ' go through each stock and collect relevant info
        
        stock = Cells(2, 1).Value
        open1 = Cells(2, 3).Value
        totvol = Cells(2, 7).Value
        l = 2
        
        For i = 2 To Cells(Rows.Count, 1).End(xlUp).Row
    
            'add up total volume for current stock
            Do While Cells(i, 1).Value = stock:
                totvol = totvol + Cells(i, 7).Value
                i = i + 1
            Loop
    
            close1 = Cells(i - 1, 6).Value
    
            change = close1 - open1
    
            'throw data in table
            Cells(l, 10).Value = stock
            Cells(l, 11).Value = change
            
            If open1 = 0 Then
                Cells(l, 12).Value = "N/A"
            Else
                Cells(l, 12).Value = change / open1
            End If
            
            Cells(l, 13).Value = totvol
            
            stock = Cells(i, 1).Value
            open1 = Cells(i, 3).Value
            totvol = Cells(i, 7).Value
    
            l = l + 1
    
        Next i
    
        
        k = 2
        biginc = Cells(k, 12).Value
        bigdec = Cells(k, 12).Value
        bigvol = Cells(k, 13).Value
        
        Do While Cells(k, 11).Value <> ""
            
            ' conditional formatting table
            If Cells(k, 11).Value >= 0 Then
                Cells(k, 11).Interior.Color = RGB(119, 252, 116)
            Else
                Cells(k, 11).Interior.Color = RGB(251, 69, 55)
            End If

            'finding greatest % increase
            If Cells(k, 12).Value >= biginc And Cells(k, 12).Value <> "N/A" Then
                biginc = Cells(k, 12).Value
                Range("p2").Value = Cells(k, 10).Value
            End If

            'finding greatest % decrease
            If Cells(k, 12).Value <= bigdec And Cells(k, 12).Value <> "N/A" Then
               bigdec = Cells(k, 12).Value
                Range("p3").Value = Cells(k, 10).Value
            End If
               
            'finding greatest total volume
            If Cells(k, 13).Value >= bigvol Then
                bigvol = Cells(k, 13).Value
                Range("p4").Value = Cells(k, 10).Value
            End If
                
            k = k + 1
            
        Loop
    
        'challenge table
        Range("p1").Value = "Ticker"
        Range("q1").Value = "Value"

        Range("o2").Value = "Greatest % Increase"
        Range("o3").Value = "Greatest % Decrease"
        Range("o4").Value = "Greatest Total Volume"

        Range("q2").Value = biginc
        Range("q3").Value = bigdec
        Range("q4").Value = bigvol

        Range("A1", "Q1").Font.Bold = True
        Columns(10).Font.Bold = True
        Range("o2", "o4").Font.Bold = True
        Range("o1", "q4").Columns.AutoFit
                
        j = j + 1
        
    Loop

End Sub

