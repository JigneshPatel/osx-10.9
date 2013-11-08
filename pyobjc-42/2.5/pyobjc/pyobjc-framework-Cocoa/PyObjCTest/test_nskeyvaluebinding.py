
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSKeyValueBindingHelper (NSObject):
    def commitEditingWithDelegate_didCommitSelector_contextInfo_(self, d, s, i):
        return None

    def commitEditing(self): return 1


class TestNSKeyValueBinding (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSMultipleValuesMarker, NSObject)
        self.failUnlessIsInstance(NSNoSelectionMarker, NSObject)
        self.failUnlessIsInstance(NSNotApplicableMarker, NSObject)

        self.failUnlessIsInstance(NSObservedObjectKey, unicode)
        self.failUnlessIsInstance(NSObservedKeyPathKey, unicode)
        self.failUnlessIsInstance(NSOptionsKey, unicode)


        self.failUnlessIsInstance(NSAlignmentBinding, unicode)
        self.failUnlessIsInstance(NSAlternateImageBinding, unicode)
        self.failUnlessIsInstance(NSAlternateTitleBinding, unicode)
        self.failUnlessIsInstance(NSAnimateBinding, unicode)
        self.failUnlessIsInstance(NSAnimationDelayBinding, unicode)
        self.failUnlessIsInstance(NSArgumentBinding, unicode)
        self.failUnlessIsInstance(NSAttributedStringBinding, unicode)
        self.failUnlessIsInstance(NSContentArrayBinding, unicode)
        self.failUnlessIsInstance(NSContentArrayForMultipleSelectionBinding, unicode)
        self.failUnlessIsInstance(NSContentBinding, unicode)
        self.failUnlessIsInstance(NSContentHeightBinding, unicode)
        self.failUnlessIsInstance(NSContentObjectBinding, unicode)
        self.failUnlessIsInstance(NSContentObjectsBinding, unicode)
        self.failUnlessIsInstance(NSContentSetBinding, unicode)
        self.failUnlessIsInstance(NSContentValuesBinding, unicode)
        self.failUnlessIsInstance(NSContentWidthBinding	, unicode)
        self.failUnlessIsInstance(NSCriticalValueBinding, unicode)
        self.failUnlessIsInstance(NSDataBinding, unicode)
        self.failUnlessIsInstance(NSDisplayPatternTitleBinding, unicode)
        self.failUnlessIsInstance(NSDisplayPatternValueBinding, unicode)
        self.failUnlessIsInstance(NSDocumentEditedBinding, unicode)
        self.failUnlessIsInstance(NSDoubleClickArgumentBinding, unicode)
        self.failUnlessIsInstance(NSDoubleClickTargetBinding, unicode)
        self.failUnlessIsInstance(NSEditableBinding, unicode)
        self.failUnlessIsInstance(NSEnabledBinding, unicode)
        self.failUnlessIsInstance(NSFilterPredicateBinding, unicode)
        self.failUnlessIsInstance(NSFontBinding, unicode)
        self.failUnlessIsInstance(NSFontBoldBinding, unicode)
        self.failUnlessIsInstance(NSFontFamilyNameBinding, unicode)
        self.failUnlessIsInstance(NSFontItalicBinding, unicode)
        self.failUnlessIsInstance(NSFontNameBinding, unicode)
        self.failUnlessIsInstance(NSFontSizeBinding, unicode)
        self.failUnlessIsInstance(NSHeaderTitleBinding, unicode)
        self.failUnlessIsInstance(NSHiddenBinding, unicode)
        self.failUnlessIsInstance(NSImageBinding, unicode)
        self.failUnlessIsInstance(NSIsIndeterminateBinding, unicode)
        self.failUnlessIsInstance(NSLabelBinding, unicode)
        self.failUnlessIsInstance(NSManagedObjectContextBinding, unicode)
        self.failUnlessIsInstance(NSMaximumRecentsBinding, unicode)
        self.failUnlessIsInstance(NSMaxValueBinding, unicode)
        self.failUnlessIsInstance(NSMaxWidthBinding, unicode)
        self.failUnlessIsInstance(NSMinValueBinding, unicode)
        self.failUnlessIsInstance(NSMinWidthBinding, unicode)
        self.failUnlessIsInstance(NSMixedStateImageBinding, unicode)
        self.failUnlessIsInstance(NSOffStateImageBinding, unicode)
        self.failUnlessIsInstance(NSOnStateImageBinding, unicode)
        self.failUnlessIsInstance(NSPredicateBinding, unicode)
        self.failUnlessIsInstance(NSRecentSearchesBinding, unicode)
        self.failUnlessIsInstance(NSRepresentedFilenameBinding, unicode)
        self.failUnlessIsInstance(NSRowHeightBinding, unicode)
        self.failUnlessIsInstance(NSSelectedIdentifierBinding, unicode)
        self.failUnlessIsInstance(NSSelectedIndexBinding, unicode)
        self.failUnlessIsInstance(NSSelectedLabelBinding, unicode)
        self.failUnlessIsInstance(NSSelectedObjectBinding, unicode)
        self.failUnlessIsInstance(NSSelectedObjectsBinding, unicode)
        self.failUnlessIsInstance(NSSelectedTagBinding, unicode)
        self.failUnlessIsInstance(NSSelectedValueBinding, unicode)
        self.failUnlessIsInstance(NSSelectedValuesBinding, unicode)
        self.failUnlessIsInstance(NSSelectionIndexesBinding, unicode)
        self.failUnlessIsInstance(NSSelectionIndexPathsBinding, unicode)
        self.failUnlessIsInstance(NSSortDescriptorsBinding, unicode)
        self.failUnlessIsInstance(NSTargetBinding, unicode)
        self.failUnlessIsInstance(NSTextColorBinding, unicode)
        self.failUnlessIsInstance(NSTitleBinding, unicode)
        self.failUnlessIsInstance(NSToolTipBinding, unicode)
        self.failUnlessIsInstance(NSValueBinding, unicode)
        self.failUnlessIsInstance(NSValuePathBinding, unicode)
        self.failUnlessIsInstance(NSValueURLBinding, unicode)
        self.failUnlessIsInstance(NSVisibleBinding, unicode)
        self.failUnlessIsInstance(NSWarningValueBinding, unicode)
        self.failUnlessIsInstance(NSWidthBinding, unicode)

        self.failUnlessIsInstance(NSAllowsEditingMultipleValuesSelectionBindingOption, unicode)
        self.failUnlessIsInstance(NSAllowsNullArgumentBindingOption, unicode)
        self.failUnlessIsInstance(NSAlwaysPresentsApplicationModalAlertsBindingOption, unicode)
        self.failUnlessIsInstance(NSConditionallySetsEditableBindingOption, unicode)
        self.failUnlessIsInstance(NSConditionallySetsEnabledBindingOption, unicode)
        self.failUnlessIsInstance(NSConditionallySetsHiddenBindingOption, unicode)
        self.failUnlessIsInstance(NSContinuouslyUpdatesValueBindingOption, unicode)
        self.failUnlessIsInstance(NSCreatesSortDescriptorBindingOption, unicode)
        self.failUnlessIsInstance(NSDeletesObjectsOnRemoveBindingsOption, unicode)
        self.failUnlessIsInstance(NSDisplayNameBindingOption, unicode)
        self.failUnlessIsInstance(NSDisplayPatternBindingOption	, unicode)
        self.failUnlessIsInstance(NSHandlesContentAsCompoundValueBindingOption, unicode)
        self.failUnlessIsInstance(NSInsertsNullPlaceholderBindingOption, unicode)
        self.failUnlessIsInstance(NSInvokesSeparatelyWithArrayObjectsBindingOption, unicode)
        self.failUnlessIsInstance(NSMultipleValuesPlaceholderBindingOption, unicode)
        self.failUnlessIsInstance(NSNoSelectionPlaceholderBindingOption, unicode)
        self.failUnlessIsInstance(NSNotApplicablePlaceholderBindingOption, unicode)
        self.failUnlessIsInstance(NSNullPlaceholderBindingOption, unicode)
        self.failUnlessIsInstance(NSRaisesForNotApplicableKeysBindingOption, unicode)
        self.failUnlessIsInstance(NSPredicateFormatBindingOption, unicode)
        self.failUnlessIsInstance(NSSelectorNameBindingOption, unicode)
        self.failUnlessIsInstance(NSSelectsAllWhenSettingContentBindingOption, unicode)
        self.failUnlessIsInstance(NSValidatesImmediatelyBindingOption, unicode)
        self.failUnlessIsInstance(NSValueTransformerNameBindingOption, unicode)
        self.failUnlessIsInstance(NSValueTransformerBindingOption, unicode)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSContentDictionaryBinding, unicode)
        self.failUnlessIsInstance(NSExcludedKeysBinding, unicode)
        self.failUnlessIsInstance(NSIncludedKeysBinding, unicode)
        self.failUnlessIsInstance(NSInitialKeyBinding, unicode)
        self.failUnlessIsInstance(NSInitialValueBinding, unicode)
        self.failUnlessIsInstance(NSLocalizedKeyDictionaryBinding, unicode)
        self.failUnlessIsInstance(NSTransparentBinding, unicode)
        self.failUnlessIsInstance(NSContentPlacementTagBindingOption, unicode)

    def testFunctions(self):
        o = NSObject.alloc().init()
        self.failUnless(NSIsControllerMarker(o) is False)
        self.failUnless(NSIsControllerMarker(NSMultipleValuesMarker) is True)

    def testMethods(self):
        o = TestNSKeyValueBindingHelper.alloc().init()
        m = o.commitEditingWithDelegate_didCommitSelector_contextInfo_.__metadata__()
        self.failUnlessEqual(m['arguments'][3]['sel_of_type'], 'v@:@Z^v')

        self.failUnlessResultIsBOOL(TestNSKeyValueBindingHelper.commitEditing)



if __name__ == "__main__":
    main()
