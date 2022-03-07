object Form1: TForm1
  Left = 241
  Top = 155
  Width = 656
  Height = 718
  VertScrollBar.Range = 200
  ActiveControl = Button1
  Caption = 'Demo of Matplotlib4D'
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = 11
  Font.Name = 'MS Sans Serif'
  Font.Pitch = fpVariable
  Font.Style = []
  PixelsPerInch = 96
  TextHeight = 13
  object Splitter1: TSplitter
    Left = 0
    Top = 0
    Width = 640
    Height = 480
    Cursor = crVSplit
    Align = alTop
    Color = clBtnFace
    ParentColor = False
    ExplicitTop = 153
  end
  object Image1: TImage
    Left = 8
    Top = 8
    Width = 624
    Height = 466
    Stretch = True
  end
  object Memo1: TMemo
    Left = 0
    Top = 633
    Width = 640
    Height = 2
    Align = alClient
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Pitch = fpVariable
    Font.Style = []
    Lines.Strings = (
      '# Import libraries'
      'import numpy as np'
      'import matplotlib'
      'import matplotlib.pyplot as plt'
      'matplotlib.use("Agg")'
      ''
      '# Input data'
      
        'vegetables = ["cucumber", "tomato", "lettuce", "asparagus", "pot' +
        'ato", "wheat", "barley"]'
      
        'farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening", "Agr' +
        'ifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]'
      'harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],'
      '                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],'
      '                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],'
      '                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],'
      '                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],'
      '                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],'
      '                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])'
      ''
      'print(vegetables)'
      'print(farmers)'
      'print(harvest)'
      ''
      'fig, ax = plt.subplots()'
      'im = ax.imshow(harvest)'
      ''
      '# We want to show all ticks...'
      'ax.set_xticks(np.arange(len(farmers)))'
      'ax.set_yticks(np.arange(len(vegetables)))'
      '# ... and label them with the respective list entries'
      'ax.set_xticklabels(farmers)'
      'ax.set_yticklabels(vegetables)'
      ''
      '# Rotate the tick labels and set their alignment.'
      
        'plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation' +
        '_mode="anchor")'
      ''
      '# Loop over data dimensions and create text annotations.'
      'for i in range(len(vegetables)):'
      '    for j in range(len(farmers)):'
      
        '        text = ax.text(j, i, harvest[i, j], ha="center", va="cen' +
        'ter", color="w")'
      ''
      'ax.set_title("Harvest of local farmers (in tons/year)")'
      'fig.tight_layout()'
      'plt.savefig("annotatedHeatmapDemo.jpg")')
    ParentFont = False
    ScrollBars = ssBoth
    TabOrder = 1
    Visible = False
  end
  object Panel1: TPanel
    Left = 0
    Top = 635
    Width = 640
    Height = 44
    Align = alBottom
    BevelOuter = bvNone
    TabOrder = 0
    object Button1: TButton
      Left = 8
      Top = 6
      Width = 115
      Height = 25
      Caption = 'Execute script'
      TabOrder = 0
      OnClick = Button1Click
    end
    object Button2: TButton
      Left = 446
      Top = 6
      Width = 91
      Height = 25
      Caption = 'Load script...'
      TabOrder = 1
      OnClick = Button2Click
    end
    object Button3: TButton
      Left = 543
      Top = 6
      Width = 89
      Height = 25
      Caption = 'Save script...'
      TabOrder = 2
      OnClick = Button3Click
    end
    object Button4: TButton
      Left = 129
      Top = 6
      Width = 112
      Height = 25
      Caption = 'Show plot'
      TabOrder = 3
      OnClick = Button4Click
    end
  end
  object Memo2: TMemo
    Left = 0
    Top = 480
    Width = 640
    Height = 153
    Align = alTop
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Pitch = fpVariable
    Font.Style = []
    ParentFont = False
    ScrollBars = ssBoth
    TabOrder = 2
    WordWrap = False
  end
  object PythonEngine1: TPythonEngine
    IO = PythonGUIInputOutput1
    Left = 72
    Top = 536
  end
  object OpenDialog1: TOpenDialog
    DefaultExt = '*.py'
    Filter = 'Python files|*.py|Text files|*.txt|All files|*.*'
    Title = 'Demo of Matplotlib4D'
    Left = 272
    Top = 528
  end
  object SaveDialog1: TSaveDialog
    DefaultExt = '*.py'
    Filter = 'Python files|*.py|Text files|*.txt|All files|*.*'
    Title = 'Save As'
    Left = 384
    Top = 536
  end
  object PythonGUIInputOutput1: TPythonGUIInputOutput
    UnicodeIO = True
    RawOutput = False
    Output = Memo2
    Left = 160
    Top = 536
  end
  object OpenPictureDialog1: TOpenPictureDialog
    Left = 288
    Top = 208
  end
end
