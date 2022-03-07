unit UnitMatplotlib4D;



interface

uses
  Classes, SysUtils,
  Windows, Messages, Graphics, Controls, Forms, Dialogs, Jpeg,
  StdCtrls, ComCtrls, ExtCtrls,
  PythonEngine, Vcl.PythonGUIInputOutput, Vcl.ExtDlgs, Vcl.Grids;

type
  TForm1 = class(TForm)
    PythonEngine1: TPythonEngine;
    Memo1: TMemo;
    Panel1: TPanel;
    Button1: TButton;
    Splitter1: TSplitter;
    Button2: TButton;
    Button3: TButton;
    OpenDialog1: TOpenDialog;
    SaveDialog1: TSaveDialog;
    PythonGUIInputOutput1: TPythonGUIInputOutput;
    Memo2: TMemo;
    Image1: TImage;
    OpenPictureDialog1: TOpenPictureDialog;
    Button4: TButton;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure Button4Click(Sender: TObject);
  private
    { Déclarations privées }
  public
    { Déclarations publiques }
  end;


var
  Form1: TForm1;

implementation

{$R *.DFM}

procedure TForm1.Button1Click(Sender: TObject);
begin
  MaskFPUExceptions(True);
  PythonEngine1.ExecStrings( Memo1.Lines );
end;

procedure TForm1.Button2Click(Sender: TObject);
begin
  with OpenDialog1 do
    begin
      if Execute then
        Memo1.Lines.LoadFromFile( FileName );
    end;
end;

procedure TForm1.Button3Click(Sender: TObject);
begin
  with SaveDialog1 do
    begin
      if Execute then
        Memo1.Lines.SaveToFile( FileName );
    end;
end;

procedure TForm1.Button4Click(Sender: TObject);
begin
  with TOpenPictureDialog.Create(self) do
    try
      Caption := 'Demo of Matplotlib4D';
      Options := [ofPathMustExist, ofFileMustExist];
      if Execute then
        Image1.Picture.LoadFromFile(FileName);
    finally
      Free;
    end;
end;

end.
