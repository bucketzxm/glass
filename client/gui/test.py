import wx
import cv

class LiveFrame(wx.Frame):

  fps = 30

  def __init__(self, parent):
    wx.Frame.__init__(self, parent, -1, title="Live Camera Feed")

    self.SetDoubleBuffered(True)
    self.capture = None
    self.bmp = None
    #self.displayPanel = wx.Panel(self,-1)

    #set up camaera init
    self.capture = cv.CaptureFromCAM(0)
    frame = cv.QueryFrame(self.capture)
    if frame:
      cv.CvtColor(frame,frame,cv.CV_BGR2RGB)
      self.bmp = wx.BitmapFromBuffer(frame.width,frame.height,frame.tostring())
      self.SetSize((frame.width,frame.height))
    self.displayPanel = wx.Panel(self,-1)

    self.fpstimer = wx.Timer(self)
    self.fpstimer.Start(1000/self.fps)
    self.Bind(wx.EVT_TIMER, self.onNextFrame, self.fpstimer)
    self.Bind(wx.EVT_PAINT, self.onPaint)

    self.Show(True)

  def updateVideo(self):
    frame = cv.QueryFrame(self.capture)
    if frame:
      cv.CvtColor(frame,frame,cv.CV_BGR2RGB)
      self.bmp.CopyFromBuffer(frame.tostring())
      self.Refresh()


  def onNextFrame(self,evt):
    self.updateVideo()
    #self.Refresh()
    evt.Skip()

  def onPaint(self,evt):
    #if self.bmp:
    wx.BufferedPaintDC(self.displayPanel, self.bmp)

    evt.Skip()

if __name__=="__main__":
    app = wx.App()
    app.RestoreStdio()
    LiveFrame(None)
    app.MainLoop()
