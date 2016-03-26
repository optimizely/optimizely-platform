import unittest

from optimizely_platform import objects


class TestAudienceConditionOption(unittest.TestCase):
  """Tests for the optimizely_platform.objects.AudienceConditionOption class."""

  def test_init__invalid_child_option_entry(self):
    child_options = [objects.AudienceConditionOption('rainy', 'Rainy'), {'value': 'snowy', 'text': 'Snowy'}]

    with self.assertRaises(ValueError) as cm:
      objects.AudienceConditionOption('weather', 'Weather', child_options)

    self.assertEqual('Each provided child option must be an instance of AudienceConditionOption.',
                     str(cm.exception))

  def test_to_dict__proper_format_without_child_options(self):
    condition_option = objects.AudienceConditionOption('sunny', 'Sunny')
    self.assertEqual({'value': 'sunny', 'text': 'Sunny', 'child_options': None}, condition_option.to_dict())

  def test_to_dict__proper_format_with_one_layer_child_options(self):
    condition_option = objects.AudienceConditionOption('sunny', 'Sunny', [objects.AudienceConditionOption('warm', 'Warm')])
    self.assertEqual({
      'value': 'sunny', 
      'text': 'Sunny', 
      'child_options': [{'value': 'warm', 'text': 'Warm', 'child_options': None}]
    }, condition_option.to_dict())

  def test_to_dict__proper_format_with_multi_layer_child_options(self):
    condition_option = objects.AudienceConditionOption('sunny', 'Sunny', 
      [objects.AudienceConditionOption('warm', 'Warm', [objects.AudienceConditionOption('humid', 'Humid')])])
    self.assertEqual({
      'value': 'sunny', 
      'text': 'Sunny', 
      'child_options': [{'value': 'warm', 'text': 'Warm', 'child_options': [{'value': 'humid', 'text': 'Humid', 'child_options': None}]}]
    }, condition_option.to_dict())


class TestAudienceCondition(unittest.TestCase):
  """Tests for the optimizely_platform.objects.AudienceCondition class."""

  def test_init__valid_creation(self):
    options = [objects.AudienceConditionOption('rainy', 'Rainy'), objects.AudienceConditionOption('snowy', 'Snowy')]

    objects.AudienceCondition('Weather', options)

  def test_init__invalid_option_entry(self):
    options = [objects.AudienceConditionOption('rainy', 'Rainy'), {'value': 'snowy', 'text': 'Snowy'}]

    with self.assertRaises(ValueError) as cm:
      objects.AudienceCondition('Weather', options)

    self.assertEqual('Each provided option must be an instance of AudienceConditionOption.',
                     str(cm.exception))


class TestVisitorSet(unittest.TestCase):
  """Tests for the optimizely_platform.objects.VisitorSet class."""

  def test_init__valid_creation(self):
    """ Ensures that we can create a valid Visitor Set."""
    try:
      visitor_set = objects.VisitorSet('cookie', 'foo', {})
    except ValueError():
      self.fail('ValueError was raised when providing valid arguments '
                'to the VisitorSet constructor')

  def test_init__invalid_creation(self):
    """Tests creation with a bogus id_type."""

    with self.assertRaises(ValueError) as cm:
      visitor_set = objects.VisitorSet('foo', 'foo', {})
    self.assertEqual('Invalid id_type specified!', str(cm.exception))
