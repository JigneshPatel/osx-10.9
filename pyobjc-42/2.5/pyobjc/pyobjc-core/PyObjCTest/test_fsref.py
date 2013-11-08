from PyObjCTools.TestSupport import *
import objc

from PyObjCTest.fsref import *

"""
@interface OC_TestFSRefHelper : NSObject
{
        }

-(FSRef)fsrefForPath:(NSString*)path;
-(NSString*)pathForFSRef:(in FSRef *)fsref;
-(void)getFSRef:(out FSRef*)fsref forPath:(NSString*)path;
-(NSString*)stringForFSRef:(FSRef)fsref;



@end
"""



class TestFSRef (TestCase):
    def testBasicInterface(self):
        self.failUnlessArgIsIn(OC_TestFSRefHelper.pathForFSRef_, 0)
        self.failUnlessArgIsOut(OC_TestFSRefHelper.getFSRef_forPath_, 0)

    def testResult(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.failUnlessIsInstance(ref, objc.FSRef)

        self.failUnlessIsInstance(ref.data, str)
        self.failUnlessIsInstance(ref.as_pathname(), unicode)

        try:
            from Carbon.File import FSRef

        except ImportError:
            pass

        else:
            self.failUnlessIsInstance(ref.as_carbon(), FSRef)

    def testArg(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.failUnlessIsInstance(ref, objc.FSRef)

        p = o.stringForFSRef_(ref)
        self.failUnlessIsInstance(p, unicode)
        self.failUnlessEqual(p, u"/Library")

    def testInput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.fsrefForPath_(u"/Library")
        self.failUnlessIsInstance(ref, objc.FSRef)

        p = o.pathForFSRef_(ref)
        self.failUnlessIsInstance(p, unicode)
        self.failUnlessEqual(p, u"/Library")

    def testOutput(self):
        o = OC_TestFSRefHelper.alloc().init()
        ref = o.getFSRef_forPath_(None, u"/Library")
        self.failUnlessIsInstance(ref, objc.FSRef)

        # Verify the fsref contents:
        p = o.stringForFSRef_(ref)
        self.failUnlessIsInstance(p, unicode)
        self.failUnlessEqual(p, u"/Library")


if __name__ == "__main__":
    main()
